from aternosapi import AternosAPI

list_cookies=["IX9AhNx9SZc0fTqRMHXRZTKyQ94BP83O3KwDTTaYDKwmfjZex1INkAxNP8klHkPpBvCCkwrJjhIsyiI0wEkaDLzPRedv4kkx3NFe","IX9AhNx9SZc0fTqRMHXRZTKyQ94BP83O3KwDTTaYDKwmfjZex1INkAxNP8klHkPpBvCCkwrJjhIsyiI0wEkaDLzPRedv4kkx3NFeIX9AhNx9SZc0fTqRMHXRZTKyQ94BP83O3KwDTTaYDKwmfjZex1INkAxNP8klHkPpBvCCkwrJjhIsyiI0wEkaDLzPRedv4kkx3NFe"]

list_headers_cookie = ["ATERNOS_SEC_sxxhb4l41v000000=w7nd9ypblbh00000; __cfduid=d140b5c6722d042280f85f9cf581e42461605100590; ATERNOS_LANGUAGE=en; _ga=GA1.2.1814112460.1605100592; _gid=GA1.2.114185433.1605100592; ATERNOS_SESSION=IX9AhNx9SZc0fTqRMHXRZTKyQ94BP83O3KwDTTaYDKwmfjZex1INkAxNP8klHkPpBvCCkwrJjhIsyiI0wEkaDLzPRedv4kkx3NFe; ATERNOS_SERVER=Qusb9yOxWjpLnAed; id5id.1st_364_nb=1; cto_bidid=zaTyJ19oQ2JXZ0lvZ0c2UFNLdzlWTzRhQkl5WTJ0SDFtNHNQcjJLQWJCcFZKYm00T0ZFdWI0OHU1cTlDT2FiV3pEQURvNFM1MFMwdGh0WWV4Q3FIRFA1d3ZCQSUzRCUzRA; cto_bundle=Va1BCV9nRmpTTVNVb1dBS2FMVmhTZVlyVVQ5U0pteTBmZzRnOVJ5R1RGdDdDQ1RFaWk3QW80bFpMdWU0aFA5RHdkY1NCeDFITlh1amdnMkFRR0Y1UFZhNWV6ektoR3piUjZEVUNNaGpNRWRDU1NjS1lDWm9yZWZ2UG4lMkJBeTVoSzJmOU0z; __gads=ID=d74a4fa981aa4b7f-22f55c3fafc400dd:T=1605100613:S=ALNI_MYzV9pu9h2E-3YO3OiFbyY9UmcCRQ; SKpbjs-unifiedid=%7B%22TDID%22%3A%221f3753e9-ded4-4bcc-91b0-0bb4815c0a2e%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222020-11-11T13%3A16%3A56%22%7D; SKpbjs-unifiedid_last=Wed%2C%2011%20Nov%202020%2013%3A16%3A56%20GMT; SKpbjs-id5id=%7B%22ID5ID%22%3A%22ID5-ZHMOJIhi6Df3iEBSVqzWDizXKSKcq0wbJ_yMWZ2SIg%22%2C%22ID5ID_CREATED_AT%22%3A%222020-11-11T13%3A16%3A56.268Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%7D; SKpbjs-id5id_last=Wed%2C%2011%20Nov%202020%2013%3A16%3A56%20GMT; GED_PLAYLIST_ACTIVITY=W3sidSI6IjhYbWoiLCJ0c2wiOjE2MDUxMDA2NTYsIm52IjoxLCJ1cHQiOjE2MDUxMDA2MTYsImx0IjoxNjA1MTAwNjU2fV0.; cto_bundle=Oj_Cvl9nRmpTTVNVb1dBS2FMVmhTZVlyVVQyb0F2VHRINkFaRGxRbG04RHNGREhYOHl1TERkVkRXR1hhWFo5R0hPSlQlMkY2N2hxZ0wxYUxGUmhzWnclMkZJOUpCVm94Ukl1bWVlMXpueGpTYWNMYkRxY3RMRW1DWFZ3dmtURk1LdGc0T0VPeWsTE: Trailers","ATERNOS_SEC_tkuh65ogzz000000=sxe3xn5w54r00000; __cfduid=d140b5c6722d042280f85f9cf581e42461605100590; ATERNOS_LANGUAGE=en; _ga=GA1.2.1814112460.1605100592; ATERNOS_SESSION=IX9AhNx9SZc0fTqRMHXRZTKyQ94BP83O3KwDTTaYDKwmfjZex1INkAxNP8klHkPpBvCCkwrJjhIsyiI0wEkaDLzPRedv4kkx3NFe; id5id.1st_364_nb=2; cto_bidid=9XOr0V9oQ2JXZ0lvZ0c2UFNLdzlWTzRhQkl5WTJ0SDFtNHNQcjJLQWJCcFZKYm00T0ZFdWI0OHU1cTlDT2FiV3pEQURvSmU0Z3pDWGpLNUhsMUpJdjV4Vm9sZyUzRCUzRA; cto_bundle=wm0sHl9nRmpTTVNVb1dBS2FMVmhTZVlyVVQ1V3FyZjlqWktUb2FWQWE1V0pxeTdmZUx5OFNHJTJCcjF6bG9yNkJZZWZxcXdnNVN6RUVqS01BWGlFYzFxbEJRTHJyb1lWSCUyRml6OHJzdiUyRnl5Q3hwd3RWY0hxYVBlMjYwRFclMkZBWWlqSTNpY3pR; __gads=ID=d74a4fa981aa4b7f-22f55c3fafc400dd:T=1605100613:S=ALNI_MYzV9pu9h2E-3YO3OiFbyY9UmcCRQ; SKpbjs-unifiedid=%7B%22TDID%22%3A%221f3753e9-ded4-4bcc-91b0-0bb4815c0a2e%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222020-11-11T13%3A16%3A56%22%7D; SKpbjs-unifiedid_last=Thu%2C%2012%20Nov%202020%2021%3A19%3A27%20GMT; SKpbjs-id5id=%7B%22ID5ID%22%3A%22ID5-ZHMOJIhi6Df3iEBSVqzWDizXKSKcq0wbJ_yMWZ2SIg%22%2C%22ID5ID_CREATED_AT%22%3A%222020-11-12T21%3A19%3A27.833Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%7D; SKpbjs-id5id_last=Thu%2C%2012%20Nov%202020%2021%3A19%3A28%20GMT; cto_bundle=hpVnOF9nRmpTTVNVb1dBS2FMVmhTZVlyVVQ1Ym5CSDc4Q200ZlBTTE5ySE5ReHZ2T2xYUUJIUlRtdm5ESk05aXBsbVBSTk9JaVVRUmR5WDI0UlBZN0FmMG5BdThEVDNFZjROdGs1UmwyNjNjTXgzTkN2JTJGQm40SWpWQlR4a29JREdTM1dvOXdWOFlCNEc3dUF3WXNNZjBWeXZ2ZyUzRCUzRA; _gid=GA1.2.1845740033.1605215957; ATERNOS_SERVER=TRDgiw1tPTHSTf9V; GED_PLAYLIST_ACTIVITY=W3sidSI6IjhYbWoiLCJ0c2wiOjE2MDUyMTYzNjEsIm52IjoxLCJ1cHQiOjE2MDUyMTYxMzYsImx0IjoxNjA1MjE2MzU4fSx7InUiOiJQRS9UIiwidHNsIjoxNjA1MjE2MjkwLCJudiI6MCwidXB0IjoxNjA1MjE2MjcxLCJsdCI6MTYwNTIxNjI3MX1d"]

list_ASEC = ["sxxhb4l41v000000:w7nd9ypblbh00000","tkuh65ogzz000000:sxe3xn5w54r00000"]
n=1
if n==1:
	headers_cookie=list_headers_cookie[0]
	cookies=list_cookies[0]
	ASEC=list_ASEC[0]

elif n==2:
	headers_cookie=list_headers_cookie[1]
	cookies=list_cookies[1]
	ASEC=list_ASEC[1]


server = AternosAPI(headers_cookie, cookies, ASEC)

def cmd(cmd,n):
	if cmd == "start":
		a=server.StartServer()
		return a
	if cmd == "stop":
		print(server.StopServer())
	if cmd == "status":
		print(server.GetStatus())
	if cmd == "info":
		print(server.GetServerInfo())

