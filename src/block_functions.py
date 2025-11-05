def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i, block in enumerate(blocks):
        blocks[i] = block.strip()
    return blocks