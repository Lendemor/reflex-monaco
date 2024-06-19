"""Reflex custom component Monaco."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx

# Some libraries you want to wrap may require dynamic imports.
# This is because they they may not be compatible with Server-Side Rendering (SSR).
# To handle this in Reflex, all you need to do is subclass `NoSSRComponent` instead.
# For example:
# from reflex.components.component import NoSSRComponent
# class Monaco(NoSSRComponent):
#     pass


class MonacoComponent(rx.Component):
    library = "@monaco-editor/react@4.6.0"

    # The language to use for the editor.
    language: rx.Var[str]

    theme: rx.Var[str] = rx.color_mode_cond("light", "vs-dark")  # type: ignore

    line: rx.Var[int] = rx.Var.create_safe(1, _var_is_string=False)

    width: rx.Var[str]

    height: rx.Var[str]


class MonacoEditor(MonacoComponent):
    """Monaco component."""

    # The React component tag.
    tag = "MonacoEditor"

    is_default = True

    # The default value to display in the editor.
    default_value: rx.Var[str]

    # The default language to use for the editor.
    default_language: rx.Var[str]

    # The path to the default file to load in the editor.
    default_path: rx.Var[str]

    # The value to display in the editor.
    value: rx.Var[str]

    on_change: rx.EventHandler[lambda e: [e]]

    on_validate: rx.EventHandler[lambda e: [e]]


class DiffMonacoEditor(MonacoComponent):
    tag = "DiffEditor"

    original: rx.Var[str]

    modified: rx.Var[str]

    original_language: rx.Var[str]

    modified_language: rx.Var[str]

    original_model_path: rx.Var[str]

    modified_model_path: rx.Var[str]

    keep_current_original_model: rx.Var[bool]

    keep_current_modified_model: rx.Var[bool]


monaco = MonacoEditor.create
monaco_diff = DiffMonacoEditor.create
