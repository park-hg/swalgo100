e[v][w]:
                d[w] = d[v] + edge[v][w]
                heappush(heap, (w, d[w]))
                visited[w] = True