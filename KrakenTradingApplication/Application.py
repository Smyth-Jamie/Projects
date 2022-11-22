import requests, json, plotly.graph_objects as go


def GET_ServerTime__TEST__():
    resp = requests.get('https://api.kraken.com/0/public/Time')

    print(resp.json())

    for property in resp.json()['result']:
        print(property, ':', resp.json()['result'][property])

def GET_SystemStatus__TEST__():
    resp = requests.get('https://api.kraken.com/0/public/SystemStatus')

    print(resp.json())

    for property in resp.json()['result']:
        print(property, ':', resp.json()['result'][property])

def GET_AssetInfo__TEST__():
    resp = requests.get('https://api.kraken.com/0/public/Assets')

    print(resp.json())

    for assetName in resp.json()['result']:
        print(assetName, '{')
        for property in resp.json()['result'][assetName]:
            print(' ', property, ':', resp.json()['result'][assetName][property])
        print('}')

def GET_AssetPairs__TEST__():
    resp = requests.get('https://api.kraken.com/0/public/AssetPairs?pair=XXBTZUSD,XETHXXBT')

    print(resp.json)

    for asset in resp.json()['result']:
        print(asset, '{')
        for property in resp.json()['result'][asset]:
            print(' ', property, ':', resp.json()['result'][asset][property])
        print('}')

def GET_TickerInformation__TEST__():
    resp = requests.get('https://api.kraken.com/0/public/Ticker')

    print(resp.json())

    for asset in resp.json()['result']:
        print(asset, '{')
        print('a: ASK [price, lot volume, lot volume]\n'
              'b: BID [price, lot volume, lot volume]\n'
              'c: Last Closed Trade [price, lot volume]\n'
              'v: Volume [Today, 24HRS]\n'
              'p: Volume Weighted Average Price [Today, 24HRS]\n'
              't: Number of Trades [Today, 24HRS]\n'
              'l: LOW [Today, 24HRS[\n'
              'h: HIGH [Today, 24HRS]\n'
              'o: Opening Price[Today]\n\n---------\n'
              )
        for property in resp.json()['result'][asset]:
            print(property, ':', resp.json()['result'][asset][property])

def GET_OHLCData__TEST__():
    resp = requests.get('https://api.kraken.com/0/public/OHLC?pair=ETHUSD')

    print(resp.json())

    for asset in resp.json()['result']:
        if asset != 'last':
            print(asset, '{\n ', '[Time, OPEN, HIGH, LOW, CLOSE, Volume Weighted Average Price, VOLUME, COUNT]')
            data = resp.json()['result'][asset]
            for row in data:
                print(' ', row)
            print('}')
        else:
            print(asset, '{\n ', resp.json()['result'][asset])
            print('}')

    time = []
    open = []
    high = []
    low = []
    close = []
    vwap = []
    count = []

    for x in range(len(data)):
        open.append(data[x][1])
        high.append(data[x][2])
        low.append(data[x][3])
        close.append(data[x][4])

    fig = go.Figure(data=[go.Candlestick(open=open,high=high,low=low,close=close,),])
    fig.show()



GET_OHLCData__TEST__()
