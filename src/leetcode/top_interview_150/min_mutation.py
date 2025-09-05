class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        queue = [[startGene, 0]]
        visited = set(startGene)
        while len(queue) > 0:
            gene, counter = queue.pop(0)
            if gene == endGene:
                return counter

            for j in range(0, len(startGene)):
                for mut in ["A", "C", "G", "T"]:
                    new_gene = gene[:j] + mut + gene[j + 1 :]

                    if new_gene in bank and new_gene not in visited:
                        queue.append([new_gene, counter + 1])
                        visited.add(new_gene)

        return -1
