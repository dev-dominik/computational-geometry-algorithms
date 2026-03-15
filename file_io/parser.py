import re
from dataclasses import dataclass
from pathlib import Path

from core import Point

FILES_DIR = Path(__file__).parent / "files"


@dataclass
class Node:
    id: int
    x: float
    y: float


@dataclass
class Element:
    id: int
    node_ids: list[int]


def _parse_line(line: str) -> list[str]:
    return re.findall(r'-?\d+(?:\.\d+)?', line)


def parse_nodes(path: Path = FILES_DIR / "nodes.txt") -> list[Node]:
    nodes = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tokens = _parse_line(line)
            nodes.append(Node(id=int(tokens[0]), x=float(tokens[1]), y=float(tokens[2])))
    return nodes

def parse_elements(path: Path = FILES_DIR / "elements.txt") -> list[Element]:
    elements = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tokens = _parse_line(line)
            elements.append(Element(id=int(tokens[0]), node_ids=[int(t) for t in tokens[1:]]))
    return elements

def get_element_points(element_id: int) -> list[Point]:
    nodes = parse_nodes()
    elements = parse_elements()

    element = next((e for e in elements if e.id == element_id), None)
    if element is None:
        return []

    points: list[Point] = []

    for node_id in element.node_ids:
        node = next((n for n in nodes if n.id == node_id), None)
        if node:
            points.append(Point(node.x, node.y))

    return points


def print_nodes(nodes: list[Node]) -> None:
    print("=== Nodes ===")
    for node in nodes:
        print(f"  Node {node.id}: x={node.x}, y={node.y}")


def print_elements(elements: list[Element]) -> None:
    print("=== Elements ===")
    for elem in elements:
        nodes_str = ", ".join(map(str, elem.node_ids))
        print(f"  Element {elem.id}: nodes=[{nodes_str}]")

