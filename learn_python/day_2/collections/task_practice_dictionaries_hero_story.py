
story1 = {"start": "Max went to the shop",
          "middle": "Max bought a can of coke",
          "end": "Max went home"}

print(story1)
print(f"The type of story1 is {type(story1)}")

print(f"A list of the keys is: {list(story1.keys())}")

print(f"The individual values of the keys are: {list(story1.values())}")

story1["character"] = "Max"

print(story1["character"])
print(f"The end. I hope you enjoyed the story about {story1["character"]}.")

