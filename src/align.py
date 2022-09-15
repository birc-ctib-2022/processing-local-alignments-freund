"""A module for translating between alignments and edits sequences."""


def align(x: str, y: str, edits: str) -> tuple[str, str]:
    """Align two sequences from a sequence of edits.

    Args:
        x (str): The first sequence to align.
        y (str): The second sequence to align
        edits (str): The list of edits to apply, given as a string

    Returns:
        tuple[str, str]: The two rows in the pairwise alignment

    >>> align("ACCACAGTCATA", "ACAGAGTACAAA", "MDMMMMMMIMMMM")
    ('ACCACAGT-CATA', 'A-CAGAGTACAAA')

    """

    seqA, seqB = [i for i in x], [j for j in y]
    aligned_seqA, aligned_seqB = [], []

    for op in edits:
        if op == "M":
            aligned_seqA.append(seqA.pop(0))
            aligned_seqB.append(seqB.pop(0))
        elif op == "D":
            aligned_seqA.append(seqA.pop(0))
            aligned_seqB.append("-")
        elif op == "I":
            aligned_seqA.append("-")
            aligned_seqB.append(seqB.pop(0))

    aligned_seqs = "".join(aligned_seqA), "".join(aligned_seqB)

    return aligned_seqs


def edits(x: str, y: str) -> str:
    """Extract the edit operations from a pairwise alignment.

    Args:
        x (str): The first row in the pairwise alignment.
        y (str): The second row in the pairwise alignment.

    Returns:
        str: The list of edit operations as a string.

    >>> edits('ACCACAGT-CATA', 'A-CAGAGTACAAA')
    'MDMMMMMMIMMMM'

    """
    edits = []

    for idx, nt in enumerate(x):
        if nt != "-" and y[idx] != "-":
            edits.append("M")
        elif nt == "-":
            edits.append("I")
        elif y[idx] == "-":
            edits.append("D")

    return "".join(edits)
