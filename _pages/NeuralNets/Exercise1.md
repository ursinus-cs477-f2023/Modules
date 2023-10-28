---
layout: exercise_pyodide
permalink: "NeuralNets/Exercise1"
title: "CS 477: Evaluating Feedforward Neural Nets"
excerpt: "CS 477: Evaluating Feedforward Neural Nets"
canvasasmtid: "189436"
canvaspoints: "2.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  next: "./Video3"
  points: 2.5
  instructions: "<p>Given a list of perceptron weight matrices <code>Ws</code> and a corresponding list of bias columns <b>bs</b>, implement the algorithm to evaluate a neural network on a particular input <code>x</code>, using the provided <code>logistic</code> function as the nonlinearity.  You will have to do this layer by layer in a loop.  As a reminder, the first layer is <code>logistic(Ws[0]*x+bs[0])</code>, where <code>*</code> means matrix multiplication.  Then the output of this is fed to <code>Ws[1]</code> and <code>bs[1]</code>, etc.</p>"
  packages: "numpy"
  goals:
    - Use a sequence of matrix multiplications to evaluate neural nets in numpy
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ref = 0.18348;
    let tol = 0.05
  correctcheck: |
    Math.abs(pyodide.globals.get("res") - ref) < tol
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == 0
      feedback: "Try again.  It looks like you're still returning 0, but you need to evaluate the neural network layers in a loop" 
    - incorrectcheck: |
        Math.abs(pyodide.globals.get("res") + 4.618) < tol
      feedback: "Try again.  It looks like you've got everything setup right in a loop, but you need to apply the logistic function to the result of each linear layer" 

files:

  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 600
    code: | 
        import numpy as np

        logistic = lambda u: 1/(1+np.exp(-u))

        def nn_forward(Ws, bs, x):
            """
            Evaluate a feedforward neural network

            Parameters
            ----------
            Ws: list of ndarray(N_{i+1}, Ni)
                Weight matrices for each layer
            bs: list of ndarray(N_{i+1})
                Bias vectors for each layer
            x: ndarray(N_0)
                Input
              
            Returns
            -------
            ndarray
                Result of neural network evaluation
            """
            ## TODO: Evaluate the neural network on an input x

            return 0 # TODO: This is a dummy



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        As = [np.random.randn(4, 3), np.random.randn(5, 4), np.random.randn(1, 5)]
        bs = [np.random.randn(4), np.random.randn(5), np.random.randn(1)]
        x = np.random.randn(3)
        res = nn_forward(As, bs, x)[0]

        
        
---
