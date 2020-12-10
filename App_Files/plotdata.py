import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns 
import io
import pandas_profiling


if __name__=='__main__':
    from PIL import Image


matplotlib.use('agg')



def regression_plot():
    df = pd.read_csv('TempRain.csv')
    sns_plot = sns.regplot(x='Temperature', y='Measure of Rain', data=df)
    plt.title('WEATHER RECORDS FROM 1960 TO 2020', size=16)
    plt.xlabel("Temperature", size=14)
    plt.ylabel('Measure of Rain' , size=14)
    image = io.BytesIO()
    sns_plot.figure.savefig(image, format = 'png')
    image.seek(0)
    return image



def create_index():
     dataset = pd.read_csv('TempRain.csv')
     report=dataset.profile_report(title='Weather - Report' , progress_bar = False)
     return report.to_file('templates/Weather_report.html')



if __name__ == "__main__":
    image = regression_plot()
    im = Image.open(image)
    im.save('Weather.png')