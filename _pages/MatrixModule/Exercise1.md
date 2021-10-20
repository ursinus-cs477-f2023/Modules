---
layout: exercise_pyodide
permalink: "MatrixModule/Exercise1"
title: "CS 477: Matrix Module Exercise"
excerpt: "CS 477: Matrix Module Exercise"
canvasasmtid: "115141"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  points: 1.5
  instructions: "Modify the <code>get_special_vector</code> code to setup an N dimensional vector <b>v</b> so that, given an <b>m x n</b> matrix <b>A</b>, <b>A x v</b> has the effect of <b>averaging</b> the columns of <b>A</b>.  You may find the commands <code><a href = \"https://numpy.org/doc/stable/reference/generated/numpy.ones.html\">np.ones</a></code> and the <code><a href = \"https://numpy.org/doc/stable/reference/generated/numpy.shape.html\">shape</a></code> field of a numpy array to be helpful."
  packages: "numpy"
  goals:
    - Initialize arrays in numpy
    - Conceptually work with matrix multiplication as a linear combination of columns
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue("" + pyodide.globals.avg + "");
  correctcheck: |
    "" + pyodide.globals.avg == "5,6,5,5,6,5,4,6,4,3"
  incorrectchecks:
    - incorrectcheck: |
        "" + pyodide.globals.avg == "0,0,0,0,0"
      feedback: "Try again. It looks like you're still returning the dummy values." 

    - incorrectcheck: |
        "" + pyodide.globals.avg == "28,33,28,25,31,26,20,34,22,16"
      feedback: "Try again.  You're very close!  Be sure to divide by the number of columns for a proper average." 


files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 450
    code: | 
          import numpy as np

          def get_special_vector(A):
            """
            Return a column vector v so that Axv has the effect of 
            averaging the columns of A

            Parameters
            ----------
            A: ndarray(M, N)
                An M x N matrix
            
            Returns
            -------
            ndarray(N)
                The special vector
            """
            return np.array([]) # TODO: This is a dummy value

  - filename: "Average Function via Matrix Multiplication"
    name: avgfn
    ismain: false
    isreadonly: true
    isvisible: true
    height: 450
    code: | 
          def average_columns(A):
            """
            Compute the average of each column of a matrix using only
            matrix multiplication and no loops

            Parameters
            ----------
            A: ndarray(M, N)
                A matrix
            
            Returns
            -------
            ndarray(M)
                A column which is the average of all other columns
            """
            M = A.shape[0]
            N = A.shape[1]
            v = get_special_vector(A)
            return A.dot(v)
              



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        A = 10*np.random.rand(10, 5)
        avg = average_columns(A)
        avg = np.array(avg, dtype=int)
        
---
