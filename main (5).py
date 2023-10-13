"""
write a function called linear search_product that takes the list of product and a target product name as input.the function should perform a linear searches to find the target product in the list and return a list of indices of all circumfernce of product if found or empty list if the product not found
"""


def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices


Products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target1 = "shoes"
target2 = "apple"
result = linearSearchProduct(Products, target1)
print(result)
