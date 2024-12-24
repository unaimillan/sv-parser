from pathlib import Path
from typing import Generator
import tree_sitter_verilog as tsverilog
from tree_sitter import Language, Node, Parser, Tree


def traverse_tree(tree: Tree) -> Generator[Node, None, None]:
    cursor = tree.walk()

    visited_children = False
    while True:
        if not visited_children:
            yield (cursor.depth, cursor.node)
            if not cursor.goto_first_child():
                visited_children = True
        elif cursor.goto_next_sibling():
            visited_children = False
        elif not cursor.goto_parent():
            break


SV_LANGUAGE = Language(tsverilog.language())
parser = Parser(SV_LANGUAGE)

SOURCES_DIR = Path('./rtl')

sv_file_path = SOURCES_DIR / 'dut.sv'

tree = parser.parse(sv_file_path.open('rb').read(), encoding='utf-8')

# print(tree.root_node)
# cursor = tree.root_node.walk()

print(*map(lambda val: f'{" " * val[0]}{val[1].type}', traverse_tree(tree)), sep='\n')
