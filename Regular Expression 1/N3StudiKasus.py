from ctypes import sizeof
import re 

text= 'Umur saya adalah 43 tahun'

bayi = '[0]'
balita = '\s*([+-]?[1-6]|-7|0)(?:\s*(?:[-,]|too?)\s*([+-]?[1-6]|-7|0))?'
anak2 = '[6-9]|[1][1-2]'
remaja = '[1][3-9]'
dewasa = '[2-4][0-9]'
tua = '[5-6][0-9]'
sangat_tua1 = '[7-9][0-9]'
sangat_tua2 = '[1][0-2]\d'

m_bayi = re.findall(bayi, text)
m_anak2 = re.findall(anak2 , text)
m_balita = re.findall(balita, text)
m_anak = re.findall(anak2 ,text)
m_remaja = re.findall(remaja , text)
m_dewasa= re.findall(dewasa, text)

print(m_anak2)
print(m_balita)
print(m_bayi)
print(m_remaja)
print(m_dewasa)
