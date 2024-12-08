# RESEARCH: WHAT IS JSON

## What does JSON stand for?

JavaScript Object Notation

## What is JSON used for?

It is a popular data-interchange format used for transmitting data between a web application
and a server. It is designed to be easy for humans to read and write, and for machines to 
parse and generate. Other use cases include
- data storage (config files, user prefs)
- data serialisation of complex data structures (such as objects and arrays) into a string 
format that can be easily transmitted and stored. 

## What is JSON written in?

It is written in **plain text**, and not a programming language, enabling it to
be independent of any one singular programming language. It was inspired by
JavaScript's object literal syntax. Most programming languages have built-in
modules or libraries designed to work with JSON data. 

## What are the advantages of JSON?

1. Readability: by humans.
2. Lightweight: using it results in smaller file sizes compared with other
formats like XML.
3. Language-agnostic: it can be used with many different programming languages.
4. Easy to parse: by computers.
5. Hierarchical structure of representing data.
6. Efficient: due to its compact structure of storing data.
7. Flexible: able to represent key-value pairs or complex objects and arrays.

## What data types can JSON store / use?

- String
- Number (integer or floating point)
- Boolean (logical value of either True or False)
- Null (a special value that indicates no value)
- Object (a collection of key-value pairs enclosed in curly braces {} )
- Array (an ordered collection of values enclosed in square brackets [] )

## What is the JSON syntax for:

- **Name-value pairs**: 
```aiignore
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
```
- **Objects**: or key-value pairs
```aiignore
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zipcode": "10001"
  },
  "hobbies": ["reading", "coding", "gaming"]
}
```

NOTE:
*name*, *age* and *city* are simple string and number values;
*address* is a nested object, which means it contains its own key-value pairs;
*hobbies* is an array, which is an ordered list of values.

- **How to separate data (key-value pairs) from one another?**

Each pair is enclosed within curly braces {}, 
and the entire JSON object is also enclosed within curly braces {}.

- **JSON arrays (these are like lists in Python)**

Each array is enclosed in square brackets [], 
and the elements within the array are separated by commas.
```
{
  "fruits": ["apple", "banana", "orange"],
  "numbers": [1, 2, 3, 4, 5]
}
```

