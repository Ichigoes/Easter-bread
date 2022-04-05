budget = float(input())
flour = float(input())
colored_eggs = 0
bread_done = 0

eggs = 0.75 * flour
milk = flour + (0.25 * flour)

recipe_price = flour + eggs + (milk * 0.25)

while budget >= recipe_price:
    colored_eggs += 3
    bread_done += 1
    budget -= recipe_price
    if bread_done % 3 == 0:
        colored_eggs -= bread_done - 2

    if budget < recipe_price:
        print(f"You made {bread_done} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break
