from flask import Flask

# create a server instance
app = Flask(__name__)

@app.route('/')
def index():
    return "Teste do metodo HTTPS"

# run the server
app.run(host="0.0.0.0", port=50100, debug=True, ssl_context="adhoc")
#https://www.google.com/search?q=como+obter+um+certificado+ssl+para+aplica%C3%A7ao+local&oq=como+obter+um+certificado+ssl+para+aplica%C3%A7ao+local&aqs=chrome..69i57.14218j0j1&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:5043fac5,vid:Cj4EIDNFMKg
#https://www.youtube.com/watch?v=WXarSJjGSFE
#https://www.youtube.com/watch?v=XJW1KB4QQCc
#https://www.cloudflare.com/pg-lp/free-ssl-tls-pt-br/?utm_source=google&utm_medium=cpc&utm_campaign=PAYGO_LATAM_BR_POR_G_Search_BG_Experiment_DNS-SSL-ADD-ON-FP&utm_content=&utm_term=certificado%20ssl&campaignid=18087281206&adgroupid=143148292511&creativeid=617965479795&&_bt=617965479795&_bk=certificado%20ssl&_bm=b&_bn=g&_bg=143148292511&_placement=&_target=&_loc=9074161&_dv=c&awsearchcpc=1&gclid=EAIaIQobChMI-Ya_-4uC_QIVDGGRCh1y5QnxEAAYASAAEgKfJ_D_BwE&gclsrc=aw.ds
