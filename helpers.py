import pandas as pd
from sklearn.linear_model import LinearRegression
def read_in(path,h_start,h_end,sign_a =1, sign_b=1,window=100):
    water = pd.read_csv(path)
    time = pd.to_numeric(water['Time'], errors="coerce")[1:]
    channelA = pd.to_numeric(water['Channel A'], errors="coerce")[1:]*sign_a
    channelB = pd.to_numeric(water['Channel B'], errors="coerce")[1:]*sign_b
    temp = channelA/0.4
    power = channelB*1.7
    smooth = temp.rolling(window=window, center=True,min_periods=0).mean()
    sem = temp.rolling(window=window,center=True,min_periods=0).sem()
    return {
        "time": time,
        "channelA": channelA,
        "channelB": channelB,
        "temp": temp,
        "power":power,
        "smooth_temp":smooth,
        "h_start":h_start,
        "h_end":h_end,
        "name": path.split('/')[1].split('_')[0],
        "sem":sem
    }

def c_tot(energy_in,delta_tg,t_gradient,integral):
    return (energy_in*delta_tg) / (delta_tg**2 - t_gradient*integral)




def plot_linear_regression(data,meta,end_h_step,right_step=0):
    """Plots linear regression and returns the model. Window: (i_end_heating + {end_h_step}) --  (i_g (+ optional right step) )"""
   
    x= data['time'][meta['i_end_h']+end_h_step:meta['i_g']+right_step]   #pd.to_numeric(x, errors="coerce")[meta['i_end_h']+end_h_step:meta['i_g']+right_step]
    y=  data['temp'][meta['i_end_h']+end_h_step:meta['i_g']+right_step]   #pd.to_numeric(y, errors="coerce")[meta['i_end_h']+end_h_step:meta['i_g']+right_step]/0.4
    x = x.values.reshape(-1, 1)  # reshape in 2D-Array for sklearn
    y = y.values
    model = LinearRegression()
    model.fit(x, y)
    
    y_pred = model.predict(x)
    
    # plt.scatter(x, y, color='blue', label='Datapoints')
    # plt.plot(x, y_pred, color='red', label='Linear Regression')
    # plt.xlabel('Time')
    # plt.ylabel('Temperature')
    # plt.title('Linear Regression')
    # plt.legend()
    # plt.show()
    
    
    # print(f'Slope: {model.coef_[0]}')
    # print(f'Bias (y-Achsenabschnitt): {model.intercept_}')
    
    return model

variables = {
    "Copper":{
    "i_start_h":973,
    "i_end_h":6208,
    "t_start_h":129.20000674,
    "t_end_h":827.20004314,
    "weight":1475,
    "c":0.385,
    "b_sign":1,
    "water":209.20000000000002,
    "t_g":1327.06673588,
    "i_g":9957,
    "M":64.546
    },
    "Alu":{
    "i_start_h":626,
    "i_end_h":5318,
    "t_start_h":82.93333766,
    "t_end_h":708.53337029,
    "weight":395.1,
    "c":0.900,
    "b_sign":1,
    "water":209.20000000000002,
    "t_g":1308.00006822,
    "i_g":9814,
    "M":26.981
    },
    "Water":{
    "i_start_h":733,
    "i_end_h": 3994,
    "t_start_h":97.20000507,
    "t_end_h":532.00002775,
    "weight":50,
    "c":4.184,
    "b_sign":-1,
    "water":0,
    "t_g": 1132.00005904,
    "i_g":8494,
    "M":0.0
    }
    


    #"lt_c_copper":

}