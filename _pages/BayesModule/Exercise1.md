---
layout: exercise_pyodide
permalink: "Module3/Exercise1"
title: "CS 477: Module 3: Naive Bayes Code"
excerpt: "CS 477: Module 3: Naive Bayes Code"
canvasasmtid: "129154"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  points: 1.5
  instructions: "<p>In this exercise, you will translate the code for a log posterior likelihood for bag of words Naive Bayes into code.  Fill in the method below to do this.  Loop through all of the keys in the counts dictionary and lookup the probabilities of the corresponding word in probs.  You can ignore the \"ugly first term\" of the multinomial count.</p><p>If you're on the network, it should submit automatically for you if you get it correct.  If you're not on the network, simply send me a screenshot of your correct solution and I'll put it in manually.</p>"
  packages: "numpy"
  goals:
    - Implement log posterior likelihood under the Naive Bayes Model
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue(pyodide.globals.res);
  correctcheck: |
    pyodide.globals.res == "-18.644"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.res == "-17.258"
      feedback: "Try again.  You're close!  Don't forget to add on the log of the prior!"
    - incorrectcheck: |
        pyodide.globals.res == "-17.008"
      feedback: "Try again.  You're close!  Don't forget to take the log of the prior!"
    - incorrectcheck: |
        pyodide.globals.res == "0.000"
      feedback: "Try again.  It seems like you're not adding anything to the probability.  Be sure to loop through all of the keys in counts and accumulate counts[key]*probs[key] over all keys"

files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
          import numpy as np

          def get_log_posterior_likelihood(counts, probs, prior):
              """
              Compute the log posterior likelihood of a set of word counts given
              probabilities in a model and a prior probability for that model.
              You can assume for simplicity that the key sets for counts and probs 
              are the same

              Parameters
              ----------
              counts: dictionary string-> int
                  The counts of a particular word in a bag of words model
              probs: dictionary string-> float
                  The smoothed log probability of a word in a model
              prior: float
                  The prior probability of the model
              """
              res = 0
              ## TODO: Fill this in
              return res



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        counts = {"computer":5, "science":3, "rocks":4}
        probs = {"computer":np.log(1/10), "science":np.log(5/10), "rocks":np.log(4/10)}
        prior = 0.25
        res = get_log_posterior_likelihood(counts, probs, prior)
        res = "{:.3f}".format(res)
        
---
