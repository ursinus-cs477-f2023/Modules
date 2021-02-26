---
layout: exercise_pyodide
permalink: "Module12/Exercise1"
title: "CS 472: Module 12: Exercise 1"
excerpt: "CS 472: Module 12: Exercise 1"
canvasasmtid: "114311"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "Fill in the <code>has_freq</code> method that determines whether a sinusoid of a particular frequency exists in a signal, using Fourier dot products."
  packages: "numpy"
  goals:
    - To use numpy element-wise operations with trig functions
    - To apply Fourier projection to check for the existence of a sinusoid
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
      
  correctcheck: |
    pyodide.globals.idx == "3"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.idx == "4"
      feedback: "Be careful!  Make sure you're taking the absolute value / magnitude and not just the real component"

files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 600
    code: | 
        import numpy as np
        def max_freq(X):
            """
            Compute the index of the maximum amplitude frequency
            in complex DFT coefficients
            
            Parameters
            ----------
            X: ndarray(K, dtype=np.complex)
                The first K coefficients of the complex DFT
            
            Returns
            -------
            int: Index of the maximum amplitude frequency
            """
            
            
            return 0 ## TODO: This is a dummy value




  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        N = 100
        n = np.arange(N)/N
        y = np.cos(2*np.pi*3*n + np.pi/4) + 0.8*np.cos(2*np.pi*4*n)
        idx = max_freq(np.fft.fft(y)[0:10])
        
---
