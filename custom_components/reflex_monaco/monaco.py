"""Reflex custom component Monaco."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx
from reflex.utils.imports import ImportDict

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

    on_change: rx.EventHandler[lambda e: [e]]

    on_validate: rx.EventHandler[lambda e: [e]]


class MonacoEditor(MonacoComponent):
    """Monaco component."""

    # The React component tag.
    tag = "MonacoEditor"

    is_default = True

    # The props of the React component.
    # Note: when Reflex compiles the component to Javascript,
    # `snake_case` property names are automatically formatted as `camelCase`.
    # The prop names may be defined in `camelCase` as well.
    # some_prop: rx.Var[str] = "some default value"
    # some_other_prop: rx.Var[int] = 1
    default_value: rx.Var[str]

    default_language: rx.Var[str]

    default_path: rx.Var[str]

    value: rx.Var[str]

    # By default Reflex will install the library you have specified in the library property.
    # However, sometimes you may need to install other libraries to use a component.
    # In this case you can use the lib_dependencies property to specify other libraries to install.
    # lib_dependencies: list[str] = []

    def add_imports(self) -> ImportDict:
        # return {**self.loading.get_imports()
        return {}


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
