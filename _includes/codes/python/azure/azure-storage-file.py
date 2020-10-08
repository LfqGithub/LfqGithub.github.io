
from azure.storage.file import FileService

mystoragename="yundong"
mystoragekey='kT5Ki4L86kRqU511wIUe2KOCJ2reSPbkW+a6gB30xWYh/o55zgZ4wihmO9QGW08SLwwph3Xzjdt/lW5rIfo1LQ=='

gjstoragename="jaymd"
gjstoragekey='yOst34HQJ3ZhVvKfXp4mpAFTDt/dt8m0BtmjZicSM3MwXLonH4yB97/R/4c/9l0dGPT4+9dExxHjgV89PGLMLA=='

file_service=FileService(account_name=mystoragename, account_key=mystoragekey,endpoint_suffix='core.chinacloudapi.cn')

file_service.create_share('myshare')
