import matplotlib.pyplot as plt #type: ignore

def plot_fuction(z_true, z_pred):
    plt.figure(figsize=(8, 5))
    plt.scatter(z_true, z_pred, color="blue", label="predictions vs. True values")
    plt.plot([min(z_true), max(z_true)], [min(z_true), max(z_true)], 't--', label="perfect fit")
    plt.xlabel("true vlaues (z_true)")
    plt.ylabel("predicted values (z_pred)")
    plt.legend()
    plt.title("modelprediciton vs. true values")
    plt.show()