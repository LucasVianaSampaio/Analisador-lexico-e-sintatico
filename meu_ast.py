# ast.py
from dataclasses import dataclass
from typing import List, Optional, Any

@dataclass
class Node:
    pass

@dataclass
class Program(Node):
    external_decls: List[Any]

@dataclass
class FunctionDef(Node):
    return_type: str
    name: str
    params: List[Any]
    body: Any

@dataclass
class VarDecl(Node):
    type: str
    name: str
    init: Optional[Any] = None

@dataclass
class Compound(Node):
    items: List[Any]

@dataclass
class If(Node):
    cond: Any
    then: Any
    otherwise: Optional[Any] = None

@dataclass
class For(Node):
    init: Optional[Any]
    cond: Optional[Any]
    step: Optional[Any]
    body: Any

@dataclass
class While(Node):
    cond: Any
    body: Any

@dataclass
class Return(Node):
    expr: Optional[Any]

@dataclass
class BinOp(Node):
    op: str
    left: Any
    right: Any

@dataclass
class UnaryOp(Node):
    op: str
    operand: Any

@dataclass
class Call(Node):
    name: str
    args: List[Any]

@dataclass
class Literal(Node):
    value: Any

@dataclass
class Identifier(Node):
    name: str

# converter árvore para dicionário para exibi-la em formato json. Melhorar a visualização
def ast_to_dict(node):
    if node is None:
        return None
    if isinstance(node, (str, int, float, bool)):
        return node
    if isinstance(node, list):
        return [ast_to_dict(n) for n in node]
    if hasattr(node, '__dataclass_fields__'):
        result = {node.__class__.__name__: {}}
        for f in node.__dataclass_fields__:
            val = getattr(node, f)
            result[node.__class__.__name__][f] = ast_to_dict(val)
        return result
    return str(node)
