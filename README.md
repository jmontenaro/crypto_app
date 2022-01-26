# crypto_app
#
#select
#  from_timestamp(to_timestamp(a.ts), 'yyyy-MM-dd') `date`
#  , a.digital_currency_code code
#  , a.close
#from
#  crypto_timeseries a
#inner join (
#  select
#    max(ts) ts,
#    digital_currency_code
#  from
#    crypto_timeseries
#  group by
#    digital_currency_code,
#    date_trunc('DAY', to_timestamp(ts))
#) b on
#  a.ts = b.ts
#  and a.digital_currency_code = b.digital_currency_code
#order by
#  code,
#  `date`;

#df = spark.sql("select * from crypto_db.crypto_monthly_ext order by code, date").collect()