import wikipediaapi
from collections import deque


class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return f'"{self.id}" connected to: [{", ".join(x.id for x in self.connected_to)}]'

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:

    def __init__(self):
        self.vertlist = {}
        self.vertnum = 0

    def add_vertex(self, key):
        if key in self.vertlist:
            return self.vertlist[key]

        self.vertnum += 1
        newvert = Vertex(key)
        self.vertlist[key] = newvert
        return newvert

    def get_vertex(self, key):
        return self.vertlist.get(key)

    def __contains__(self, key):
        return key in self.vertlist

    def add_edge(self, f, t, weight=0):
        if f not in self.vertlist:
            self.add_vertex(f)
        if t not in self.vertlist:
            self.add_vertex(t)
        self.vertlist[f].add_neighbor(self.vertlist[t], weight)

    def get_vertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

    def __str__(self):
        return '\n'.join(str(x) for x in self.vertlist.values())

    def __len__(self):
        return len(self.vertlist)


def build_wiki_graph(pagename, max_depth=3, max_count=1000):
    wiki = wikipediaapi.Wikipedia('Team00 (merlin@example.com)', 'en')
    page = wiki.page(pagename)
    if not page.exists():
        return None

    graph = Graph()
    queue = deque()
    queue.appendleft((page, 0))
    depth = 0
    count = 0

    while len(queue) and len(graph) < max_count:
        page, depth = queue.pop()
        if depth > max_depth:
            break

        print(page.title)
        see_also = page.section_by_title('See also')
        print(see_also)
        if see_also is None:
            continue

        vertex = graph.add_vertex(page.title)

        for pagename in filter(
            None,
            (x.strip() for x in see_also.text.split('\n'))
        ):
            page = wiki.page(pagename)
            if not page.exists():
                continue
            graph.add_edge(vertex.id, pagename, weight=1)
            if len(graph) >= max_count:
                break
            queue.appendleft((page, depth + 1))

    return graph


def main():
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vertlist)
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)

    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))

    graph = build_wiki_graph('Python (Programming language)')
    print(graph)


if __name__ == '__main__':
    main()

