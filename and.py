from utils.all_utils import prepare_data, save_plot
from utils.model import Perceptron
import pandas as pd

def main(data, modelName, plotName, eta, epochs):

    df = pd.DataFrame(data)

    X, y = prepare_data(df)



    model = Perceptron(eta=ETA, epochs=EPOCHS)
    model.fit(X, y)

    _ = model.total_loss()
    #3 Saving themodelˍ
    model.save(filename=modelName, model_dir="model_or")

    ## SAving the plot
    save_plot(df, model, filename=plotName)

if __name__=="__main__":

    AND = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y" : [0,0,0,1]
    }
    ETA = 0.1 # 0 and 1
    EPOCHS = 10
    main(data=AND, modelName='and.model', plotName='and.png', eta=ETA, epochs= EPOCHS)
