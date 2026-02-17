# urllib

# result = []
# for x in data:
#     if x % 2 == 0:
#         result.append((x + 1) * 10)

def is_honest(x):
    return not x % 2

def normalize(x):
    return (x + 1) * 10

result = (
    normalize(x)
    for x in data
    if is_honest(x)
)