---
layout: exercise_pyodide
permalink: "Module2/Exercise1"
title: "CS 472: Module 2: Part 1"
excerpt: "CS 472: Module 2: Part 1"
canvasasmtid: "111002"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2" 
  points: 1.5
  instructions: "<p></p>"
  packages: "numpy,matplotlib"
  goals:
    - To manipulate variables and types in python
    - To apply arithmetic expressions in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("8 Buses, 2 Vans.4 Buses, 1 Vans.0 Buses, 1 Vans")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("8.0 Buses, 2 Vans.4.0 Buses, 1 Vans.0.0 Buses, 1 Vans")
      feedback: "Try again.  You've got the right answer!  But make sure num_buses is an int by saying <code>num_buses = int(num_buses)</code>." 
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
          import matplotlib.pyplot as plt
          import numpy as np
          import io, base64
          x = np.random.randn(100)



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        plt.figure(figsize=(8, 4))
        plt.plot(x)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = 'data:image/png;base64,' + base64.b64encode(buf.read()).decode('UTF-8')
        
---
