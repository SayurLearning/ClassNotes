import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()   

# define a list of numbers
numbers = [10, 5, 20, 15, 8, 25, 30, 18, 12, 25, 25, 30]

# get a list of tuples containing the index and value of each element
indexed_numbers = list(enumerate(numbers))

# sort the list of tuples by the value of each element
sorted_numbers = sorted(indexed_numbers, key=lambda x: x[1], reverse=True)

# get the index of the top 3 values, handling ties
top_values = sorted_numbers[:3]
top_indexes = [i for i, num in indexed_numbers if num in [val for _, val in top_values]]

# print the top 3 indexes
print(top_indexes)
