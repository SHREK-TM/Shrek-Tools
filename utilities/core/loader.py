# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import importlib.util
import os
import re

from utilities.core.tool_order import (
    SPECIAL_TOOL_IDS,
    SPECIAL_TOOL_NAMES,
    TOOL_NAMES,
    TOOL_ORDER,
    order_key_for_module,
)

TOOLS_PACKAGE = "utilities.tools"
TOOLS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tools")
SLOTS_PER_PAGE = 27
SPECIAL_MODULES = frozenset({"settings", "discordserver"})
SKIP_MODULES = frozenset({"__init__"})

_ENTRY_RE = re.compile(r"^\s*def (run|main|main_menu)\s*\(", re.MULTILINE)

_tools_cache = None


def _module_display_name(module_name: str) -> str:
    return module_name.replace("_", " ").replace("-", " ").upper()


def _has_entry_point(file_path: str) -> bool:
    try:
        with open(file_path, encoding="utf-8", errors="ignore") as handle:
            return bool(_ENTRY_RE.search(handle.read()))
    except OSError:
        return False


def _resolve_run(mod, module_name: str):
    run_fn = getattr(mod, "run", None)
    if callable(run_fn):
        return run_fn

    main_menu_fn = getattr(mod, "main_menu", None)
    if callable(main_menu_fn):
        return main_menu_fn

    main_fn = getattr(mod, "main", None)
    if callable(main_fn) and order_key_for_module(module_name) in TOOL_ORDER:
        return main_fn

    return None


def _load_and_run_module(module_name: str, *args, **kwargs):
    file_path = os.path.join(TOOLS_DIR, f"{module_name}.py")
    if not os.path.isfile(file_path):
        print(f"[Loader] Fichier introuvable : {file_path}")
        return None

    full_name = f"{TOOLS_PACKAGE}.{module_name}"
    try:
        spec = importlib.util.spec_from_file_location(full_name, file_path)
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except BaseException as exc:
        if isinstance(exc, (KeyboardInterrupt, SystemExit)):
            raise
        print(f"[Loader] Failed to load {module_name}: {exc}")
        return None

    run_fn = _resolve_run(mod, module_name)
    if not run_fn:
        print(f"[Loader] Aucun point d'entrée valide trouvé dans {module_name}")
        return None

    return run_fn(*args, **kwargs)


def _apply_order_and_name(entry: dict, module_name: str):
    order_key = order_key_for_module(module_name)
    if order_key in TOOL_ORDER:
        entry["order"] = TOOL_ORDER[order_key]
    if order_key in TOOL_NAMES:
        entry["name"] = TOOL_NAMES[order_key]
    if module_name in SPECIAL_TOOL_NAMES:
        entry["name"] = SPECIAL_TOOL_NAMES[module_name]


def _make_runner(module_name: str):
    def runner(*args, **kwargs):
        return _load_and_run_module(module_name, *args, **kwargs)
    return runner


def _build_tool_entry(module_name: str):
    file_path = os.path.join(TOOLS_DIR, f"{module_name}.py")
    if not os.path.isfile(file_path) or not _has_entry_point(file_path):
        return None

    entry = {
        "module": module_name,
        "name": _module_display_name(module_name),
        "order": None,
        "special": module_name in SPECIAL_MODULES,
        "run": _make_runner(module_name),
    }

    _apply_order_and_name(entry, module_name)
    return entry


def _list_tool_modules() -> list[str]:
    modules = []
    for filename in os.listdir(TOOLS_DIR):
        if not filename.endswith(".py"):
            continue
        module_name = filename[:-3]
        if module_name in SKIP_MODULES:
            continue
        modules.append(module_name)
    return sorted(modules)


def _assign_auto_slots(tools: list) -> list:
    regular = [t for t in tools if not t.get("special")]
    special = [t for t in tools if t.get("special")]

    regular.sort(
        key=lambda t: (
            t.get("order") if t.get("order") is not None else 9999,
            t.get("module", ""),
        )
    )

    for idx, tool in enumerate(regular, start=1):
        tool["id"] = str(idx).zfill(2)
        tool["page"] = ((idx - 1) // SLOTS_PER_PAGE) + 1

    for tool in special:
        module = tool.get("module", "")
        tool["id"] = SPECIAL_TOOL_IDS.get(module, "!")

    return special + regular


def discover_tools():
    global _tools_cache
    if _tools_cache is not None:
        return _tools_cache

    tools = []
    seen = set()

    for module_name in SPECIAL_MODULES:
        entry = _build_tool_entry(module_name)
        if entry:
            tools.append(entry)
            seen.add(module_name)

    for module_name in _list_tool_modules():
        if module_name in seen or module_name in SPECIAL_MODULES:
            continue
        entry = _build_tool_entry(module_name)
        if entry:
            tools.append(entry)
            seen.add(module_name)

    _tools_cache = _assign_auto_slots(tools)
    return _tools_cache


def reload_tools():
    global _tools_cache
    _tools_cache = None


def get_tools_by_page(page: int):
    return [
        t
        for t in discover_tools()
        if int(t.get("page") or 0) == page and not t.get("special")
    ]


def get_page_count() -> int:
    regular = [t for t in discover_tools() if not t.get("special")]
    if not regular:
        return 1
    return max(int(t.get("page") or 1) for t in regular)


def normalize_tool_id(tool_id: str) -> str:
    normalized = tool_id.strip().upper()
    if normalized.isdigit():
        return normalized.zfill(2)
    return normalized


def get_tool_by_id(tool_id: str):
    normalized = normalize_tool_id(tool_id)
    for t in discover_tools():
        if normalize_tool_id(str(t.get("id", ""))) == normalized:
            return t
    return None


def get_special_tool(tool_id: str):
    normalized = tool_id.upper()
    for t in discover_tools():
        if t.get("special") and str(t.get("id", "")).upper() == normalized:
            return t
    return None
