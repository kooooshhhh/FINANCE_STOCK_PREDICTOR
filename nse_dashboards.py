from nselib import capital_market as cap
from nselib import derivatives
import streamlit as lit
                   
lit.header('Indian Stock financial Dashboard')
instrument = lit.sidebar.selectbox('Instrument Type', 
                                   options=("NSE Equity Market","NSE Derivatives Market"))
if instrument == "NSE Equity Market":

    data_info = lit.sidebar.selectbox('Data to extract: ', options=('get_price_volume_and_deliverable_position_data',
                   'price_volume_data',
                   'get_price_volume_data',
                   'deliverable_position_data',
                   'get_deliverable_position_data',
                   'india_vix_data',
                   'get_india_vix_data',
                   'index_data',
                   'get_index_data',
                   'bulk_deal_data',
                   'get_bulk_deal_data',
                   'block_deals_data',
                   'get_block_deals_data',
                   'short_selling_data',
                   'get_short_selling_data',
                   'bhav_copy_with_delivery',
                   'bhav_copy_equities',
                   'bhav_copy_indices',
                   'equity_list',
                   'fno_equity_list',
                   'nifty50_equity_list',
                   'market_watch_all_indices',
                   'fii_dii_trading_activity'))

    if (data_info=='equity_list') or (data_info =='fno_equity_list') or (data_info=='market_watch_all_indices') or (data_info=='nifty50_equity_list'):
            data= getattr(cap,data_info)
    if (data_info=='bhav_copy_equities') or (data_info =='bhav_copy_with_delivery'):
            date=lit.sidebar.text_input('Date','01-02-2024')
            data= getattr(cap,data_info)(date)
    if (data_info=='block_deals_data') or (data_info =='bulk_deal_data') or (data_info =='bulk_deal_data') or (data_info =='bulk_deal_data') or (data_info =='bulk_deal_data'):
            period= lit.sidebar.text_input('Period','1M')
            data= getattr(cap,data_info)(period=period)


lit.write(data)
