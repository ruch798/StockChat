from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Classifier import test
import matplotlib.pyplot as plt
import json
import time
import os

data={"ongc": [["Oil & Natural Gas Corporation Limited has informed the Exchange regarding a press release dated Jun 19, 2019, titled \"Press Release w.r.t. Subsidiary company - ONGC Videsh Limited\".", [0.069, 0.839, 0.091, 0.1531]], ["Press Release w.r.t. Subsidiary company  ONGC Videsh Limited, a wholly-owned subsidiary of the Company, along with its joint venture partners of Mozambique Rovuma Offshore Area 1 announces Final Investment Decision for initial two LNG train Project Development. In this regard a ''''Press Release'''' is being issued as per attachment", [0.04, 0.915, 0.046, 0.0772]], ["Intimation under the SEBI (Prohibition of Insider Trading) Regulations, 2015", [0.0, 1.0, 0.0, 0.0]], ["Oil & Natural Gas Corporation Ltd has informed BSE that the Board of Directors of the Company at its Meeting held on May 30, 2019, inter alia, have recommended a final dividend @ Rs. 0.75/- (Seventy five paisa only) per equity share of Rs. 5/- each, for the Financial Year 2018-19, subject to necessary approval of members at the ensuing Annual General Meeting.", [0.0, 0.854, 0.146, 0.8225]], ["In terms of Regulation 30 and 33 of the SEBI (Listing Obligation and Disclosure Requirements), Regulations, 2015, we submit herewith Standalone and Consolidated Audited Financial Results for the quarter/ year ended 31st March, 2019 along with Audit Report for Financial Year ended 31st March 2019.", [0.0, 1.0, 0.0, 0.0]], ["Intimation regarding issue of duplicate shares", [0.0, 0.694, 0.306, 0.296]], ["Oil & Natural Gas Corporation Ltd has informed BSE that a meeting of the Board of Directors of the Company is scheduled to be held on May 30, 2019, inter alia, to consider and approve the standalone and consolidated audited Financial Results of the Company for the quarter and year ended March 31, 2019 and recommendation of Final Dividend, if any, for the year 2018-19, subject to approval of the shareholders.", [0.0, 0.923, 0.077, 0.6808]], ["OIL AND NATURAL GAS CORPORATION LTD.has informed BSE that the meeting of the Board of Directors of the Company is scheduled on 30/05/2019 ,inter alia, to consider and approve Pursuant to Regulation 29(1) read with Regulation 33 of the SEBI Listing Obligations and Disclosure Requirements) Regulations, 2015 we hereby inform that a meeting of the Board of Directors of the Company is scheduled to be held on Thursday, the 30th May, 2019, inter-alia, to consider and approve the standalone and consolidated audited Financial Results of the Company for the quarter and year ended 31st March, 2019 and recommendation of Final Dividend, if any, for the year 2018-19, subject to approval of the shareholders.", [0.0, 0.946, 0.054, 0.7456]], ["Intimation regarding issue of duplicate shares", [0.0, 0.694, 0.306, 0.296]], ["Format of Initial Disclosure to be made by an entity identified as a Large Corporate.  Sr. No. Particulars Details  1Name of CompayOIL AND NATURAL GAS CORPORATION LTD. 2CININE213A01029 3 Outstanding borrowing of company as on 31st March / 31st December, as applicable (in Rs cr) 0 4Highest Credit Rating during the previous FY NA 4aName of the Credit Rating Agency issuing the Credit Rating mentioned in (4)Not Applicable 5Name of Stock Exchange# in which the fine shall be paid, in case of shortfall in the required borrowing under the frameworkBSE     We confirm that we are a Large Corporate as per the applicability criteria given under the SEBI circular SEBI/HO/DDHS/CIR/P/2018/144 dated November 26, 2018. No   Name of the Company Secretary: M E V SELVAMM   Designation: COMPANY SECRETARY  EmailId: selvamm_mev@ongc.co.in  Name of the Chief Financial Officer: SUBHASH KUMAR  Designation: DIRECTOR (FINANCE)  EmailId: dir_fin@ongc.co.in    Date: 29/04/2019 Note: In terms para of 3.2(ii) of the circular, beginning F.Y 2022, in the event of shortfall in the mandatory borrowing through debt securities, a fine of 0.2% of the shortfall shall be levied by Stock Exchanges at the end of the two-year block period. Therefore, an entity identified as LC shall provide, in its initial disclosure for a financial year, the name of Stock Exchange to which it would pay the fine in case of shortfall in the mandatory borrowing through debt markets. ", [0.057, 0.837, 0.106, 0.8602]]], "sbin": [["With reference to news appeared in www.asianage.com dated June 18, 2019 quoting \"Jet Air lands in NCLT as banks give up on revival\", State Bank of India has submitted to BSE a copy of Clarification is enclosed.", [0.0, 1.0, 0.0, 0.0]], ["Disclosure under Regulation 44(3) and 30 of SEBI (LODR) Regulations 2015: Outcome of 64th Annual General Meeting", [0.0, 1.0, 0.0, 0.0]], ["Disclosure under Regulation 30 of SEBI (LODR) Regulations 2015", [0.0, 1.0, 0.0, 0.0]], ["State Bank Of India has informed the Exchange regarding Analysts/Institutional Investor Meet/Con. Call Updates", [0.0, 1.0, 0.0, 0.0]], ["The Exchange has sought clarification from State Bank of India on June 18, 2019, with reference to news appeared in www.asianage.com dated June 18, 2019 quoting \"Jet Air lands in NCLT as banks give up on revival\"The reply is awaited.", [0.027, 0.973, 0.0, -0.0258]], ["Disclosure under Regulation 30 of SEBI (LODR) Regulations 2015", [0.0, 1.0, 0.0, 0.0]], ["The Exchange had sought clarification from State Bank of India with reference to the media report, \"SBI, banks gave defaulting Sterling owners Rs 1.3k cr guarantees\".State Bank of India response is enclosed.", [0.0, 1.0, 0.0, 0.0]], ["The Exchange has sought clarification from State Bank Of India with respect to news item captioned ??SBI, banks gave defaulting Sterling owners Rs 1.3k cr guarantees??. The response from the Company is awaited.", [0.03, 0.857, 0.112, 0.6072]], ["Intimation under Regulation 30 of SEBI (LODR) Regulations 2015", [0.0, 1.0, 0.0, 0.0]], ["Intimation under Regulation 39(3) of SEBI (LODR) Regulations 2015", [0.0, 1.0, 0.0, 0.0]]],"tatamotors": [["Tata Motors slips 3% on Moody's downgrade", [0.0, 1.0, 0.0, 0.0]], ["Moody's downgrades Tata Motors with negative outlook on JLR worries", [0.448, 0.552, 0.0, -0.7579]], ["Hold Tata Motors; target of Rs 185: ICICI Direct", [0.0, 1.0, 0.0, 0.0]], ["If Nifty holds 11,780, bounceback towards 12,050 possible", [0.0, 0.722, 0.278, 0.4019]], ["Buy on dips as long as Nifty trades above crucial support of 11,780; Tata Motors among 5 stocks to bet on", [0.0, 0.769, 0.231, 0.6597]], ["Accumulate Tata Motors; target of Rs 192: Prabhudas Lilladher", [0.0, 1.0, 0.0, 0.0]], ["Stocks in the news: Tata Motors, Wipro, SAIL, Music Broadcast, PFC, Tiger Logistics, Reliance Nippon", [0.0, 1.0, 0.0, 0.0]], ["Tata Motors global sales dip 23% in May", [0.0, 1.0, 0.0, 0.0]], ["Tata Motors falls after weak UK sales by Jaguar Land Rover", [0.225, 0.775, 0.0, -0.4404]], ["Summer of discontent: No let-up in sales gloom for automakers", [0.42, 0.58, 0.0, -0.7003]]], "techm": [["Hold Tech Mahindra; target of Rs 845: ICICI Direct", [0.0, 1.0, 0.0, 0.0]], ["Tech Mahindra inks deal with Airbus for cabin, cargo design engineering", [0.0, 1.0, 0.0, 0.0]], ["Accumulate Tech Mahindra; target of Rs 880: Dolat Capital", [0.0, 1.0, 0.0, 0.0]], ["Buy Tech Mahindra; target of Rs 900: Motilal Oswal", [0.0, 1.0, 0.0, 0.0]], ["Tech Mahindra collaborates with Cisco, deploys solutions at Hyderabad campus", [0.0, 0.841, 0.159, 0.1779]], ["India Inc cheers Modi-led BJP's victory, but calls for inclusive economic growth", [0.0, 0.647, 0.353, 0.6652]], ["Tech Mahindra betting big on telecom sector's revival for growth, says CFO", [0.0, 0.809, 0.191, 0.3818]], ["What should investors do with Tech Mahindra post Q4: buy, sell or hold?", [0.0, 1.0, 0.0, 0.0]], ["Ideas for Profit | Tech Mahindra posts a subdued Q4; caution advised", [0.0, 0.756, 0.244, 0.4404]], ["Tech Mahindra Consolidated March 2019 Net Sales at Rs 8,892.30 crore, up 10.4% Y-o-Y", [0.0, 1.0, 0.0, 0.0]]], "tatasteel": [["Tata Steel Europe CEO Hans Fischer to step down", [0.0, 1.0, 0.0, 0.0]], ["Indian steel industry to outperform global peers; 6 stocks that can return in double digits", [0.0, 1.0, 0.0, 0.0]], ["In a first, Tata Steel ventures into steel scrap recycling", [0.0, 1.0, 0.0, 0.0]], ["Tata Steel, JSW Steel fall 2% as CLSA turns bearish on earnings risk", [0.149, 0.851, 0.0, -0.2732]], ["Tata Steel ends 5% higher, ends 4-day losing streak after Goldman Sachs maintains buy", [0.167, 0.833, 0.0, -0.3818]], ["Stocks in the news: Tata Steel, DHFL, Yes Bank, Voltas, India Cements, Adani Green, Suzlon", [0.0, 0.838, 0.162, 0.4019]], ["EU blocks Thyssenkrupp-Tata steel merger plan", [0.275, 0.725, 0.0, -0.2263]], ["Here's how to use covered calls to reduce cost of holding a stock", [0.0, 1.0, 0.0, 0.0]], ["Hold Tata Steel; target of Rs 475: ICICI Direct", [0.0, 1.0, 0.0, 0.0]], ["NCLT approves Tata Steel takeover of Bhushan Energy", [0.0, 0.556, 0.444, 0.5859]], ["Indias coal import rises 13% to 21 MT in April", [0.0, 1.0, 0.0, 0.0]]], "bajaj": [["Accumulate Bajaj Auto; target of Rs 3631: Arihant Capital", [0.0, 1.0, 0.0, 0.0]], ["Buy Bajaj Auto; target of Rs 3484: KR Choksey", [0.0, 1.0, 0.0, 0.0]], ["Exclusive | Aprilia 150cc twins launch put on backburner; Piaggio to focus on EVs, BS-VI", [0.0, 0.897, 0.103, 0.128]], ["Buy Bajaj Auto; target of Rs 3330: HDFC Securities", [0.0, 0.784, 0.216, 0.296]], ["Bajaj Auto sales rise 3% in May to 4.19 lakh units", [0.0, 1.0, 0.0, 0.0]], ["Bajaj Auto gains 3% after May sales beat analyst expectations", [0.0, 0.789, 0.211, 0.34]], ["Bajaj Auto\u2019s margin to remain lower than historical highs, eyes \u2018complete product portfolio\u2019", [0.155, 0.845, 0.0, -0.296]], ["Hold Bajaj Auto; target of Rs 3250: Sharekhan", [0.0, 1.0, 0.0, 0.0]], ["Lawsuit filed against Royal Enfield in the US on patent violation", [0.362, 0.638, 0.0, -0.6249]], ["Ideas for Profit|Bajaj Auto Q4: Margin hurts, but long-term outlook positive", [0.129, 0.564, 0.307, 0.5927]]]}

mean={'SBIN': {'Last': 282.97550143266466, 'VWAP': 283.10681948424053, 'Turnover': 642220824461246.38}, 'TATAMOTORS': {'Last': 201.66991869918692, 'VWAP': 202.0130894308943, 'Turnover': 378398678663597.13}, 'ONGC': {'Last': 158.12154471544713, 'VWAP': 158.13386178861791, 'Turnover': 169391331169044.72}, 'TECHM': {'Last': 733.68272357723572, 'VWAP': 733.63207317073147, 'Turnover': 239695542020609.75}, 'BAJAJ-AUTO': {'Last': 2807.5270325203242, 'VWAP': 2808.6369918699193, 'Turnover': 157829449381829.28}, 'TATASTEEL': {'Last': 530.50630081300835, 'VWAP': 531.18699186991898, 'Turnover': 454572221236910.69}}
std={'SBIN': {'Last': 24.583907718899638, 'VWAP': 24.447131388995221, 'Turnover': 360113994875547.94}, 'TATAMOTORS': {'Last': 37.706686096979602, 'VWAP': 37.944427445874759, 'Turnover': 299459256142027.38}, 'ONGC': {'Last': 11.485562838251122, 'VWAP': 11.445482659021884, 'Turnover': 176704513160544.56}, 'TECHM': {'Last': 53.247450569727974, 'VWAP': 52.955088435677418, 'Turnover': 149415737857737.09}, 'BAJAJ-AUTO': {'Last': 158.35711895880749, 'VWAP': 156.74914067494367, 'Turnover': 137250956883623.56}, 'TATASTEEL': {'Last': 42.15155330556766, 'VWAP': 42.234124037649643, 'Turnover': 237320001685546.59}}


app = Flask(__name__)

counter=0

@app.route('/',methods=["POST", "GET"])
def index():
	return render_template("chatbot.html")
	
@app.route('/webservice')
def webservice():
	result=int(request.args.get("param1"))*100
	return jsonify(result="img.png")
	
	


@app.route('/predictbuy')
def predictbuy():
	global counter,mean,std
	name=request.args.get("param1").lower()
	result=test.predict1(name)
	ans=[]
	for i in range(len(result)):
		ans.append(int(result[i][0][0]*std[name.upper()]["Last"]+mean[name.upper()]["Last"]))
	#print(result)
	os.system("rm static/img0.png")
	plt.plot([i for i in range(len(ans))],ans)
	location="img"+str(0)+".png"
	plt.savefig("static/"+location)
	plt.show()
	print(ans)
	print(result)
	counter+=1
	
	#return jsonify(zero=zero[0][0][0],one=one[0][0][0],two=two[0][0][0],three=three[0][0][0],four=four[0][0][0],five=five[0][0][0],six=six[0][0][0],seven=seven[0][0][0],eight=eight[0][0][0],nine=nine[0][0][0])
	company=data[name]
	arr=[]
	for i in company:
		arr.append([i[1][3],i[0]])
	arr.sort()
	n=len(arr)
	
	time.sleep(0.1);
	
	#summ=arr[0][0]+arr[1][0]+arr[n-1][0]+arr[n-2][0]
	if arr[0][0]>-arr[n-1][0]:
		return jsonify(graph=location, message="You can BUY today because:-<br>"+arr[0][1]+"<br><br>"+arr[1][1]+"<br>The target price may reach "+str(max(ans))+" after "+str((ans.index(max(ans))+1))+" days so you can sell then")
	else:
		return jsonify(graph=location, message="You should not BUY today as the stock price may go down because:-<br>"+arr[n-1][1]+"<br><br>"+arr[n-2][1])
		

	
@app.route('/predictsell')
def predictsell():
	global counter,mean,std
	name=request.args.get("param1").lower()
	price=request.args.get("param2").lower()
	result=test.predict1(name)
	ans=[]
	os.system("rm static/img0.png")
	for i in range(len(result)):
		ans.append(int(result[i][0][0]*std[name.upper()]["Last"]+mean[name.upper()]["Last"]))
	print(result)
	
	plt.plot([i for i in range(len(ans))],ans)
	location="img"+str(0)+".png"
	plt.savefig("static/"+location)
	plt.show()
	counter+=1
	
	#return jsonify(zero=zero[0][0][0],one=one[0][0][0],two=two[0][0][0],three=three[0][0][0],four=four[0][0][0],five=five[0][0][0],six=six[0][0][0],seven=seven[0][0][0],eight=eight[0][0][0],nine=nine[0][0][0])
	company=data[name]
	arr=[]
	for i in company:
		arr.append([i[1][3],i[0]])
	arr.sort()
	n=len(arr)
	#summ=arr[0][0]+arr[1][0]+arr[n-1][0]+arr[n-2][0]

	
	time.sleep(0.1);
	
	if arr[0][0]>-arr[n-1][0]:
		return jsonify(graph=location, message="You must HOLD the stocks for now because:-<br>"+arr[0][1]+"<br><br>"+arr[1][1]+"<br>The target price may reach "+str(max(ans))+" after "+str((ans.index(max(ans))+1))+" days, so you may sell then")
	else:
		return jsonify(graph=location, message="You should SELL today as the stock price may go down because:-<br>"+arr[n-1][1]+"<br><br>"+arr[n-2][1])
	
	

if __name__ == '__main__':
   app.run(debug=True)
