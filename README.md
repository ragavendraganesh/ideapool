Implementing Resful Service

AccessTokens
Refresh JWT
Endpoint
POST /access-tokens/refresh
Parameters
Name	Description
refresh_token required	Refresh token of the existing user
Request
Route
POST /access-tokens/refresh
Headers
Content-Type: application/json
Host: example.org
Cookie:
Body
{
  "refresh_token": "the-token-str-2"
}
Response
Status
200
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"8c434067e0e2c85ffa673c3221ed3304"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 26b955a3-8b3a-4ae3-a899-cab5bc5e944b
X-Runtime: 0.029432
Content-Length: 835
Body
{
  "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODUsImlkIjoiaXI5dGNrcDhiIiwiZW1haWwiOiJlbWFpbC0zQHRlc3QuY29tIiwibmFtZSI6Im5hbWUtMyJ9.2r6D2ql0syQuMYB5S49SAHwaY8K0OgO7JaMXuOagnYp8ZuCyqivBw7YcuDKjpjmFjYJFogoBD3-vHGXJKppz198x4fbSiWtDPOwz4w26yPjE_iLQeyoyAYYTtNVEsP6BKcJHbKM_V_hDVVVeTeWzs_jTlrIrVsIWKR4PvOORzNnKHjgXW5QCyhXOjP-Wz9PesXTZcXva6va4BnPREN5x8fVP0kMvo7X4XzFtv2Q_AbY3h9eYne3E-rPQGPjbc4Yp16fw3uet1L7uFVyaDBBdT_IWnbrw0VhZNqcf_xrKcDVyMjZexMXyByeCKzF_XlY0_PJ6nAeEjNYFl8IHUCxMGai0nc-N2oELgG0t0lzOBZiM-9vZLP9znyM9BEYiBKMf2C0mVzCrT_Pu4nC4DwOrxMCiJW5tA7nyOTDJ2sPbXn0iL88GdX_4MvxHZOSf8GTOxLm9TNTw8uyb4pc8fg2ssN-6gBnB2SJH1MuMsiUG0Tog7NZe8UYXu_GtS6ktsvFGChu1VVF7erysbIySNeBTunCx-XoEBRoj45bsNs-QlXw10TiDwZHq4n8pwwFKR2oI8uB16rG1omg48pbbkUvsZdy0bcr1itaWaTKkmpz6LMIUvHWlpv6RYMiGFWM5qkAupP4fvfHeKml92GlSvMJsleu-hjSas-n1a_tUPksk4r4"
}
User login
Endpoint
POST /access-tokens
Parameters
Name	Description
email required	Email of the existing user
password required	Password of the existing user
Request
Route
POST /access-tokens
Headers
Content-Type: application/json
Host: example.org
Cookie:
Body
{
  "email": "email-1@test.com",
  "password": "the-Secret-123"
}
Response
Status
201
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"66599270884f5b0d89e61fcdf1c5dde2"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 01475484-18d2-4a90-8569-f679845a2bf7
X-Runtime: 0.185575
Content-Length: 954
Body
{
  "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODUsImlkIjoiaXI5dGNhcHExIiwiZW1haWwiOiJlbWFpbC0xQHRlc3QuY29tIiwibmFtZSI6Im5hbWUtMSJ9.X5Fj-EJDMuYKId_HH_INJN3UXGX3wCcfkoXZycvAAIV0RwmQJ_QiaDpbZvzqYnjg30bu1eO6d3MCBbF0QKzv5eFHF0V7fFWJhyd7bBen_my81biZiNj1UVGvKgxOi3BS2prjBOCTBoPJFr8bYxmrqgF3hyflIE8SMFj-e3hfF7VGWlrFxWFsZlvzgFBWNsGKmrrQNWvkEumKPkBLMOa__19JwoWVfBIp5B_uEctKaSgCeSlghjgvHSXmMYq06sh_zzLZfPZZQ0dbqaehfalG6US4nKo7JIiix7-VYp92b2TFahaTWO3LyngusKztQfjsKrOACniMwyMqr1fdV_tSsRi-jEDEtjxrbLLMge7yW9xOarQ618OPgWe1hG1KwM_WhgsZMuPTkl_5wxTKH9wPygy6WHxV-UqDczaFqF87uI_M2IFPr_QGpRaQQyNxSeQYxyGw0IrCR2doo0OoLiDXUZBNku-RWI9s9H5Eqm9YIg33P6mXtN39kz5Sim6Jg_x5tZ22PTm-Mu6bdtIZBogQflZiBJt1eji_hH8nJDFuh3ZxMCon4yeTL7m8ZWuf8-_Z5zfSltk_ePIqWt3c4GnMU9kd5sgjrJCuLwof00HTXFFjYLBmPpWtNfvQ6_gOjws-MKQkGH35Vail5-nvujfI0itzKWc36h3qUPOQG8p0jsw",
  "refresh_token": "6c0e3c51a51b8df21da34d63eadfcf6d9b54fe2a7acd88bc135ead0eb6e1969a4e7faf75c14b8b6e787b6cc4722afd9465eb"
}
User logout
This API will logout current user

Endpoint
DELETE /access-tokens
Parameters
Name	Description
refresh_token required	Refresh token for the existing user
Request
Route
DELETE /access-tokens
Headers
Content-Type: application/json
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODUsImlkIjoiaXI5dGNobDE2IiwiZW1haWwiOiJlbWFpbC0yQHRlc3QuY29tIiwibmFtZSI6Im5hbWUtMiJ9.Yn7ZDN6sWKeHki9z9LbY48gc3lXjVyZkNL7zBlYII1sXzbNnfUvKNi5QGyMv9avxTptW0SgOwJuRsTeD_H_UNN8S7Y0xEPXHd1iZ7Bh_KLTVxLa0Of8UCZeua4j9O2qkh_fv110Chld4k1nn9VMcSZdGs2w8IjiqWVHop_VVr_UTKLYH_azbas78k9n7jQHufSq4Y49t2eznZt_gq_jMIjmXg6DfMB3q-qQx8yJRw7Q6J2Z89QTfjRqiL_uH5mVFwfDdrNGi2Yl0FHiKDnjyZySfu0GgZcaKpDOUK2SCrGkMNzzpORScHZe6pTENv-PxTWd9Zm-7xsUVTNxBisqXPiE0HUUIaK37BGb_tlOUzc9s4ll0Kek42fUONqbLw28Ps9rjC-BllqbiNlmqY4sHFcQtlZZwViKexiHNn57PPmqV85HOrkesP-WEHHsXzdyAOqr05NAz4A_3bf-T8hKtilsD-2cHwDXYQcppRDSn-pUT5Kxoh9HwzNjHhy3s9fXr0OV-kL-plIy9K9wa_DOqNOOYQ5zOMDqPqopZR-QsHVdzbfmuByfn_FFvZBWNCfxZTjFNdF81huCebH-hl1C43hdzasJU2uA-BvTkNNFkdeQARwRIL-bb-3TJ9Gve3dLC0t79M7h1hhy-W6cGIw0YkhiyqZ5D7YwQE0bnI52GUVo
Host: example.org
Cookie:
Body
{
  "refresh_token": "the-token-str-1"
}
Response
Status
204
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Cache-Control: no-cache
X-Request-Id: 14af0e05-28c3-411b-887a-0f734285daf6
X-Runtime: 0.012214
Vary: Origin
Current User
Get current user's info
Endpoint
GET /me
Request
Route
GET /me
Headers
Content-Type: application/json
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODYsImlkIjoiaXI5dGNudGZnIiwiZW1haWwiOiJlbWFpbC00QHRlc3QuY29tIiwibmFtZSI6Im5hbWUtNCJ9.z4TifqkE9-Bw7k_4XMctNOXV3_yoRqaFh_AS6UdeIASpGnbn5dvhLfT1JlLjWM3y_0VnLzmofo9UC1dkm5IB6waElLF5wzncQUT04L2Kpn4QhU9e0oPEeziwb4geeiJtrgsLRJx3gSkH6ha6NgwaYdmZf5alu9hejb3VIvR-zY0oqLJhCA7-BnyqZmnmIZxBHpKOk9V20XxkFzyicKuUEwQrwwYwoY5v5I1DTHgFV7hmkMvqKqifTmDztheZqijw5m_YfP9rOANXISBS4KgIJrS5Gavc03uX1SDmKd3KHgtiV8Fqvtf9rvImoKZAQiuYX92nDg-CjA5z8i7Is7qkG1tMXyV4GyRFm2KvbEWMpoBlezXXmO5Tr0CtvlSBZWgxbwpzUYklSDJcqnhSenSLQlabqwHaxvQjYoPQLU8wzLAEh_DvPqkpQMyr3gywfk6-I9OSmyiQmhUShKBZsY3KrZSHBV8914KYdt4TCsK6eay1CGHe8m1ptaL1wG-dYvja6xqOxbN3iyH6Oi7O5afP7iKwVelDQzAe4XXVgjfDhWenuyThV01YhWq_yRjpPvftuV3yA19rQnuo2zFAjp6dAN1Ml41ICaBQMr1NYkAlDzEZSpo9RrHRakACeuO83pGQRPZ8ERlsr3ClGnM0fQ_I2f0VwsVtro4jXDDJjwVlhxI
Host: example.org
Cookie:
Response
Status
200
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"c547b0fe6f7c536c5c20e89d364678a0"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: d0ffbacb-41a5-4551-9719-8091152c1081
X-Runtime: 0.048111
Content-Length: 140
Body
{
  "email": "email-4@test.com",
  "name": "name-4",
  "avatar_url": "https://www.gravatar.com/avatar/b36aafe03e05a85031fd8c411b69f792?d=mm&s=200"
}
Ideas
Create idea
Endpoint
POST /ideas
Parameters
Name	Description
content required	Content (maximum 255 characters)
impact required	Impact score (requires integer between 1 to 10, 10 being the highest impact)
ease required	Ease score (requires integer between 1 to 10, 10 being the easiest to implement)
confidence required	Confidence score (requires integer between 1 to 10, 10 being the most confident)
Request
Route
POST /ideas
Headers
Content-Type: application/json
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODYsImlkIjoiaXI5dGNybGJ4IiwiZW1haWwiOiJlbWFpbC01QHRlc3QuY29tIiwibmFtZSI6Im5hbWUtNSJ9.FnG9qIdwTPqSBt5DbOjamM29p2DdiJuUXC3aUKEdNh749CWuSxx1kuT7oNCSjCqi3D7g5XuRLXTAtNDdkQWrGraIsdnXdTT36meiSVp15avRMXOp_wEOVillbMPkgED3oBQfM6KmK9EC-FU8sALn1_NAvmre9B6Jyz_ewcfKur-w4hw5c1xRa3Ca6Ff_8-J8QazscO7bn0Q5wMF-rQNAwXkx8xsPFQK_gZ8H-oZxxvy7QZIAkpE2agKIiemNxsGcs4HE-Bv9lSaS8NKFXa7CgWSYDhsBfIApy-DVBbD9zIHJVEWYC81AqnURc4acsW8zvLQslXo0QJrY2F15Oeq7Otz3lI6QB14oLxymW5c8Sh5VpCueygIJokALW-sAubgSAxZM-Iz2MMLpj8nvvFwSnyQzbdDKMKjeqK0fJwkAVWoMhR_n-LdNNDlGmqACcpsBvKuSPVc22mf1nk7iOTgHLef84-LjIcugEZ9TVDKaohrD6gXRZzgqfHb5kImi0ydlzxnDceZDnu4ODtFKlsx-2QncYf118p7jBb_o0gNYYayFLM9SPXI4vzSY6icRnfYEv2JCw9bNBvtxMdvvm5FDskM7miMKTFpvZDeYWGeSvX5k17zVzXY_YGgDWcKHRa986msIIY6ooFkEiFSkmWNugNL3TeQQGGvcKm0Z0aXZ6gE
Host: example.org
Cookie:
Body
{
  "content": "the-content",
  "impact": 8,
  "ease": 8,
  "confidence": 8
}
Response
Status
201
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"91c744964358e217fe5c7cae7917e76a"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 9e6b5cbe-c9a7-4e5e-84ec-f9263f2fd746
X-Runtime: 0.058592
Content-Length: 121
Body
{
  "id": "ir9tctewu",
  "content": "the-content",
  "impact": 8,
  "ease": 8,
  "confidence": 8,
  "average_score": 8.0,
  "created_at": 1524210786
}
Delete idea
Endpoint
DELETE /ideas/:id
Request
Route
DELETE /ideas/ir9tcznb6
Headers
Content-Type: application/json
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODYsImlkIjoiaXI5dGN6azVkIiwiZW1haWwiOiJlbWFpbC03QHRlc3QuY29tIiwibmFtZSI6Im5hbWUtNyJ9.Yx9Khaa5_kWmPKmGd4dYH7AXvICniZ_wgzR9ByrExs1sAp33-cpoM9K_oUlZJ2ZHQTNJ8-G666azE9CI9sjJTDhfv8Nr_An8L6nUZa-G1Dg8xXKUMoF5-6I3dePYXeu4sw-fGPH_vwGfTcSHaGk3mPy0Lc3PrCaB-_i-48hzFgvqrzKQ2ZjUXtgqPlF_ouPYtfvvrZGdIaiVH0ga0T915ZQSwgXoUO8HtmjqNYx-0JZg8ZeHnbH-WuTIlCCUzA11JLvilXgakyUeQ1adtSkmkH4ZwzEd9TR9N6yIuticA5gdHOsKzqKLWHQcuFd1TXL6AVd9mV7Pa6RBuZHEUY5BgPLT1LftMnQuBaSqVDosTNs_fSb6sOiM6I61GgzG2y-n7wPkgAFSHyXbe6kb1m7qN3QWYedg4FkTeIZYgm2hvQEjAHuVlh1MUXm4B6ISqiZxwy_gXE4f1AZn42dVnp0WAhwNH96va3zfNNY71plA4AE54ng7_KvnLVy9TFsUJF3y1Y3CIiFuu4chS1QPhNVLRmh4BiuQg2yPo8A-xZ_FivUCE5g6B-y-KkauJpUHpCjqQi3JvOx_uFCieLH4TWgC8BRnjWi5Trx8l5AeurVa_ZxJRntZvyZw9gO2KZd4DQc6jdiuSl81xY0WyuE9kUkgquO0QALm0qhnNfPMUagK9jM
Host: example.org
Cookie:
Response
Status
204
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Cache-Control: no-cache
X-Request-Id: aca850d7-0df9-47fe-9c4d-1977942a77be
X-Runtime: 0.012323
Vary: Origin
Get a page of ideas (1 page = 10 ideas)
Endpoint
GET /ideas
Parameters
Name	Description
page	A single page of ideas (integer > 0)
Request
Route
GET /ideas
Headers
Content-Type: application/json
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODYsImlkIjoiaXI5dGQyaTB6IiwiZW1haWwiOiJlbWFpbC04QHRlc3QuY29tIiwibmFtZSI6Im5hbWUtOCJ9.v819bsdMiyPFBL3OeVFugzlydiXwOqwDUDxX3iGUtHmUhHrF6vXpyYZ_jLl0BysS5qwYyaqqFJOlOlK3jcACg1qUhwX5zeoXGB2V0RD0MUdgTWaRcgiVO_aLHFGJYXZyZb1qufgJuKj8uo3fezmJ355U1-X79A6hxOA2nehE-UgOVpQyKQhh79MiP6SuuHuqujJq98hc43TSVe_y2RnuAIFQcQNrgh4a0v_3_yOhM3bIcRSCA-7cmqF4BIUKXn6o5-Z9R0yl5Sgvdl13wBj99KDXr32_S3TgE_nt5hvE2OyZfBjg8LVo2c-XGLezXk2bh2tcpCp1T2vI8GNYA7RWcYyJi5v0wVed7xK-Tme0MiryWz8IjQJI7_HbZ6dLVKiZ7IEy6ETqsuC8YmFamkVNBKCApS1A9Hx26KMqvOep61TxT5bugKo1hF7a97I5TEnJHqjVxsg_nnYeg1GKdDlgdji3Trp11btNnH0rUAP1URXzYY94IQpS4JWUQrfAJ4lt3GaHId6lNMcuhlOvkxq3O2N05PzxLQV-8kWoLt8A3hhOe1cO-YIu0TmxzSLS8LWz4CVsiS6mS7ZoBQsxWOGjL-OU2wjRlbzx3di12r7sPLj9wfUOWNoDA832ZSpEwkx0KWsEdPEYZD6na2gpRIWr6j5Dyc_5GPKh57pLfLB67zE
Host: example.org
Cookie:
Response
Status
200
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"95c019a976656206509434dfef12ebc1"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 85df4d03-2305-4a85-a895-34692b353416
X-Runtime: 0.021043
Content-Length: 395
Body
[
  {
    "id": "ir9td2tvq",
    "content": "the-content",
    "impact": 3,
    "ease": 8,
    "confidence": 8,
    "average_score": 6.333333333333333,
    "created_at": 1524210786
  },
  {
    "id": "ir9td2p51",
    "content": "the-content",
    "impact": 2,
    "ease": 8,
    "confidence": 8,
    "average_score": 6.0,
    "created_at": 1524210786
  },
  {
    "id": "ir9td2lz8",
    "content": "the-content",
    "impact": 1,
    "ease": 8,
    "confidence": 8,
    "average_score": 5.666666666666667,
    "created_at": 1524210786
  }
]
Update idea
Endpoint
PUT /ideas/:id
Parameters
Name	Description
content required	Content (minimum 1 character, maximum 255 characters)
impact required	Impact score (requires integer between 1 to 10, 10 being the highest impact)
ease required	Ease score (requires integer between 1 to 10, 10 being the easiest to implement)
confidence required	Confidence score (requires integer between 1 to 10, 10 being the most confident)
Request
Route
PUT /ideas/ir9tcw81s
Headers
Content-Type: application/json
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODYsImlkIjoiaXI5dGN3NDNqIiwiZW1haWwiOiJlbWFpbC02QHRlc3QuY29tIiwibmFtZSI6Im5hbWUtNiJ9.Isa_VkFVJ85E4kWRBRhSurEXKcAjCykDKDl0RYJ7oc0JbAFMR3YaHmi9rUORpQHDGBu8dtQejrFzv2s2NSDWb2NuzB3SnT1WKMM3q-w5MBmfab53gBK8JitU8fUzjIQQ3qoOOdBOrqG7C5Yfvx9WtRObApYMBjdHcYc3ZZD2cgPwOukq2o4pmuxWdDYLvPBsEPMJEK_VaLv-GFbqfxnOGzcM1_lKwYTuTtLVygmC12L8MTAP4i4daAUo9C3gctDUgm1oft8kAS0E9o9l7lTPHfFIhVaisEfdEdxo6MIJ56vLDq8ozyKU0EOvJBaAAlELKoQnOOX3rYqrPGiFH2Q1TXcRs2i2N_MizONYRxF8GdncD1Y4TFt_4Zw8B3T-tpWd_t-W300pVRFNWKK4jLCA7_wqcziXemzEvzZ-XvP9XRQyHG6r4DY6-vKUNcy-vpnj3RRjJNX08XG8_rRP_yp4BytHFEv0ahu_nUkLpBcN1YnZHDj1Vxdxm6lIm4mPHEZTs5I_l0DcjoIiq6DpGTzhtgMVJvoVtvYvOG_ZfC9LcJHmrxg4mURPCafK_zA043oZ5yL6SF62riT6m_ZWNLnilNHJAoV7PvH0BbBi96O2-hzlULFRNmFL-ustQXBH4HhvS1LKtR12MUfV4OeoNqWwnBG2_bTjO4joXm14J7qLnV8
Host: example.org
Cookie:
Body
{
  "content": "the-content",
  "impact": 8,
  "ease": 8,
  "confidence": 8
}
Response
Status
200
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"c2c0e968a038de5a5c9fcfa9682fe40b"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 048b9e3c-1d98-447b-ba2b-7975862c6a1e
X-Runtime: 0.029936
Content-Length: 121
Body
{
  "id": "ir9tcw81s",
  "content": "the-content",
  "impact": 8,
  "ease": 8,
  "confidence": 8,
  "average_score": 8.0,
  "created_at": 1524210786
}
Users
Signup
Endpoint
POST /users
Parameters
Name	Description
email required	Email
name required	Full name
password required	Password (at least 8 characters, including 1 uppercase letter, 1 lowercase letter, and 1 number)
Request
Route
POST /users
Headers
Content-Type: application/json
Host: example.org
Cookie:
Body
{
  "email": "jack-black@codementor.io",
  "name": "Jack Black",
  "password": "the-Secret-123"
}
Response
Status
201
Headers
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
ETag: W/"462d245d2e13572a7a51d22442195c82"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: e5216222-f2c0-455f-a68b-7a311b4988e8
X-Runtime: 0.134269
Content-Length: 970
Body
{
  "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1MjQyMTEzODYsImlkIjoiaXI5dGQ2c3c3IiwiZW1haWwiOiJqYWNrLWJsYWNrQGNvZGVtZW50b3IuaW8iLCJuYW1lIjoiSmFjayBCbGFjayJ9.nxoNY8AUi314V5zGsxgFYPMUytOApt1URBjS65ICFUv5BmzrXTkOKfOJqmKtJmJeKjeq7agY083rgnsn4D8SKkG0mCbL67pH2ZeT7U8HQ5bFAO3kvtmk0VRKzz5GkwSRl2h6ZbhqxUsLuPGxSzvyxsphpqH2rumSerzhQlrm78V-5CYidFPczNJfA7CCQtYpuQqm-rM-9g15SPj7zT64SbLXq5O-ioJjyxo22ihcEq_pe-AZ5Iab-IeJoacH-19BkRejV319_-KeXx3mVw-TQKpSWgr3ApjB1G5IHpG7EUM9FVhX0qr6rh-ll6deKLa6arGEOg0atprBcS3HNUyd8d-bvfLXPE8DVooGteLQhZC0v7fqdkczPvzI24e_jufxZGM_nQvbJ6reab-KulIRcSNmrxWX5WpkBcM-G74W8tQKezT4smCFjgsm2VxI395U4a2SVYl7ziLHLKZ6cxJSIG6AjsW4TEP3UxW9XH82bu4FEktKUuYfQlAdM_Ajtjx2wFGSb7s0e0ggQFYHEkov_1KRA4Qex7Ou4qE21piSIkp4zZ2qAJelaVPqZgHtoD96lIabjJkir9wZM36hhByV6rE58s-kZWmD56x9iOtOIFrvDq4KpQmmQ8ALnhYhx2CPFchKA1rZDURdyYfa8o75YSTd6RdB0mFvfncSCRfvEB0",
  "refresh_token": "6fa08ad5a189408373c9fddaa0780ddeb3db7b804acd364c2486e300d184af9c9fbe2a33d0c33b90894613f87dcc76078e6f"
}