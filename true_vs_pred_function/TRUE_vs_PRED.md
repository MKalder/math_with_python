# True vs. Predicted Function

The **Sum of Squared Residuals (SSR)**, also called the **loss function**, is used in optimization problems. It is commonly applied in machine learning to measure a model’s error.

## Residual

A residual is the difference between the actial and the estimated value

$\text{Residuum} = y_i - \hat{y}_i$

## Example Income calculation

model estimated value = 3.500 € \
acutal income = 3.800 €

$\text{300 €} = 3.800 € - 3.500€ $

## Squared Residuals

Instead of summing up all the residuals, we will square them because, without squaring, they could cancel each other out.

$\text{SSR} = \sum (y_i - \hat{y}_i)^2$


| Datapoint | Actual value (y)  | Prediction ($ \hat{y} $)| Residuum \( y - $ \hat{y} $ \) | Residuum² |
|------------:|--------------------------:|----------------------:|----------------------:|------------:|
| 1          | 5                        | 4                    | 1                    |           1|
| 2          | 10                       | 8                    | 2                    |          4|
| 3          | 15                       | 14                   | 1                    |         1 |

$\text{SSR} = 1 + 4 + 1 = 6$

A small SSR indicates a good model fit.

# Example true function vs model prediction

Imagine we are modeling a measurement that depends on two variables, \( x \) and \( y \). The true function could be expressed as:

$
z = (x - 3)^2 + (y - 2)^2 + \sin(3x) \cos(2y) + \text{noise}
$

Where:
- The quadratic error component:
  $
  (x - 3)^2 + (y - 2)^2
  $
- The nonlinear disturbance:
  $
  \sin(3x) \cos(2y)
  $
- The noise is a random deviation that occurs in real-world data.

## Modelprediction 

Our model differs slightly from the true function, so it will produce errors.

$
\hat{z} = (x - 2.5)^2 + (y - 1.5)^2 + sin(2.5 * x) cos(1.8 * y)
$

## SSR Calculation

$\text{SSR} = \sum (z_{true} - \hat{z})^2$

## Summary

- **Residuals** measure individual prediction errors.  
- **Squaring residuals** prevents cancellation and penalizes larger errors more.  
- **SSR quantifies overall model accuracy** lower SSR means a better model fit.