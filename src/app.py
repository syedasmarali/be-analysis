import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import os

def display_ingredient_cost(ingredient_quantity, ingredient_cost, ingredient_name, unit):
    ingredient_cost_recipe = float(ingredient_quantity) * float(ingredient_cost.replace(',', '.'))

    # Format the output with commas
    formatted_ingredient_quantity = f"{ingredient_quantity:.1f}".replace('.', ',')
    formatted_cost_ingredient = f"{ingredient_cost_recipe:.3f}".replace('.', ',')

    # Display the result
    st.markdown(
        f"<h6 style='text-align: left; color: black;'>{formatted_ingredient_quantity} {unit} of {ingredient_name} Cost: <span style='color: green;'>{formatted_cost_ingredient}</span></h6>",
        unsafe_allow_html=True
    )

    return ingredient_cost_recipe

# Page layout
st.set_page_config(layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>Break Even Analysis Holly Guacamole</h1>", unsafe_allow_html=True)

# Add a divider
st.divider()

# Enter recipe ingredients
st.sidebar.header("Guacamole Recipe Ingredients")
with st.sidebar.expander("Enter Guacamole Recipe Ingredients", expanded=False):
    # Entering thai guacamole recipe
    st.markdown("<h4 style='text-align: center;'>Thai Guacamole</h4>", unsafe_allow_html=True)
    avocado_thai = st.number_input('Avocado in Pcs.', min_value=0.0, max_value=100.0, value=2.0)
    lime_thai = st.number_input('Lime in Pcs.', min_value=0.0, max_value=100.0, value=0.5)
    red_chili_thai = st.number_input('Red Chili in Grams', min_value=0.0, max_value=100.0, value=3.0)
    onion_thai = st.number_input('Onion in Grams', min_value=0.0, max_value=100.0, value=25.0)
    coriander_thai = st.number_input('Coriander in Grams', min_value=0.0, max_value=100.0, value=8.0)

    # Entering kid friendly guacamole recipe
    st.markdown("<h4 style='text-align: center;'>Kid Friendly Guacamole</h4>", unsafe_allow_html=True)
    avocado_kid = st.number_input('Avocados in Pcs.', min_value=0.0, max_value=100.0, value=2.0)
    lime_kid = st.number_input('Limes in Pcs.', min_value=0.0, max_value=100.0, value=0.5)
    mayonnaise_kid = st.number_input('Mayonnaise in Grams', min_value=0.0, max_value=100.0, value=30.0)
    tomato_kid = st.number_input('Tomato in Grams', min_value=0.0, max_value=100.0, value=80.0)
    garlic_kid = st.number_input('Garlic in Grams', min_value=0.0, max_value=100.0, value=7.0)

    # Entering fiery guacamole recipe
    st.markdown("<h4 style='text-align: center;'>Fiery Guacamole</h4>", unsafe_allow_html=True)
    avocado_fiery = st.number_input('Avocado in Pc.', min_value=0.0, max_value=100.0, value=2.0)
    lime_fiery = st.number_input('Lime in Pc.', min_value=0.0, max_value=100.0, value=0.5)
    jalapeno_chili_fiery = st.number_input('Jalapenos in Grams', min_value=0.0, max_value=100.0, value=6.0)
    onion_fiery = st.number_input('Onions in Grams', min_value=0.0, max_value=100.0, value=25.0)
    tobasco_fiery = st.number_input('Tobasco in ml', min_value=0.0, max_value=100.0, value=4.0)

# Enter recipe ingredients
st.sidebar.header("Guacamole Per Day Demand")
with st.sidebar.expander("Enter Guacamole Per Day Demand", expanded=False):
    # Enter recipe demand
    thai_demand = st.number_input('Thai Guacamole Per Day Demand', min_value=0, max_value=1000, value=15)
    kid_demand = st.number_input('Kid Friendly Guacamole Per Day Demand', min_value=0, max_value=1000, value=28)
    fiery_demand = st.number_input('Fiery Guacamole Per Day Demand', min_value=0, max_value=1000, value=7)
    thai_monthly_demand = thai_demand * 30
    kid_monthly_demand = kid_demand * 30
    fiery_monthly_demand = fiery_demand * 30


# Demand visualization
st.markdown("<h2 style='text-align: center;'>Product Demand</h2>", unsafe_allow_html=True)
thai_monthly_demand = thai_demand * 30
kid_monthly_demand = kid_demand * 30
fiery_monthly_demand = fiery_demand * 30

# Data
monthly_demand_data = {
    'Gucamole': ['Thai Guacamole', 'Kid Friendly Guacamole', 'Fiery Guacamole'],
    'Monthly Demand': [thai_monthly_demand, kid_monthly_demand, fiery_monthly_demand]
}

# Create a DataFrame
df = pd.DataFrame(monthly_demand_data)

# Create a bar plot using Plotly
fig = go.Figure()

# Add bars to the figure
fig.add_trace(go.Bar(
    x=df['Gucamole'],
    y=df['Monthly Demand'],
    marker_color='green',
    text=df['Monthly Demand'],
    textposition='auto',
    textfont=dict(size=18)
))

# Update layout
fig.update_layout(
    title='Monthly Demand of Guacamole',
    xaxis_title='Guacamole',
    yaxis_title='Monthly Demand',
    template='plotly_white'  # Optional: change template for better visuals
)

# Display the figure in Streamlit
st.plotly_chart(fig)

# Add a divider
st.divider()

# Ingredients demand
st.markdown("<h2 style='text-align: center;'>Ingredients Demand</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

# Demand for thai guacamole ingredients
with col1:
    daily_demand_avocado_thai = avocado_thai * thai_demand
    daily_demand_lime_thai = lime_thai * thai_demand
    daily_demand_red_chili_thai = red_chili_thai * thai_demand
    daily_demand_onion_thai = onion_thai * thai_demand
    daily_demand_coriander_thai = coriander_thai * thai_demand

    # Data
    monthly_demand_data = {
        'Ingredient': ['Avocado', 'Lime', 'Red Chili', 'Onion', 'Coriander'],
        'Daily Demand': [
            daily_demand_avocado_thai,
            daily_demand_lime_thai,
            daily_demand_red_chili_thai,
            daily_demand_onion_thai,
            daily_demand_coriander_thai
        ]
    }

    # Create a DataFrame
    df_thai_ingredients = pd.DataFrame(monthly_demand_data)

    # Calculate monthly demand (assuming 30 days)
    df_thai_ingredients['Monthly Demand'] = df_thai_ingredients['Daily Demand'] * 30

    # Create a bar plot using Plotly
    fig = go.Figure()

    # Add bars for daily demand
    fig.add_trace(go.Bar(
        x=df_thai_ingredients['Ingredient'],
        y=df_thai_ingredients['Daily Demand'],
        name='Daily Demand',
        marker_color='green',
        text=df_thai_ingredients['Daily Demand'],
        textposition='auto',
        textfont=dict(size=14)
    ))

    # Add bars for monthly demand
    fig.add_trace(go.Bar(
        x=df_thai_ingredients['Ingredient'],
        y=df_thai_ingredients['Monthly Demand'],
        name='Monthly Demand',
        marker_color='blue',  # Change color for distinction
        text=df_thai_ingredients['Monthly Demand'],
        textposition='auto',
        textfont=dict(size=14)
    ))

    # Update layout
    fig.update_layout(
        title='Daily and Monthly Demand of Thai Guacamole Ingredients',
        xaxis_title='Ingredients',
        yaxis_title='Demand',
        barmode='group',  # Group bars together
        template='plotly_white'  # Optional: change template for better visuals
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig)

# Demand for kid friendly guacamole ingredients
with col2:
    daily_demand_avocado_kid = avocado_kid * kid_demand
    daily_demand_lime_kid = lime_kid * kid_demand
    daily_demand_mayonaise_kid = mayonnaise_kid * kid_demand
    daily_demand_tomato_kid = tomato_kid * kid_demand
    daily_demand_garlic_kid = garlic_kid * kid_demand

    # Data
    monthly_demand_data = {
        'Ingredient': ['Avocado', 'Lime', 'Mayonnaise', 'Tomato', 'Garlic'],
        'Daily Demand': [
            daily_demand_avocado_kid,
            daily_demand_lime_kid,
            daily_demand_mayonaise_kid,
            daily_demand_tomato_kid,
            daily_demand_garlic_kid
        ]
    }

    # Create a DataFrame
    df_kid_ingredients = pd.DataFrame(monthly_demand_data)

    # Calculate monthly demand (assuming 30 days)
    df_kid_ingredients['Monthly Demand'] = df_kid_ingredients['Daily Demand'] * 30

    # Create a bar plot using Plotly
    fig = go.Figure()

    # Add bars for daily demand
    fig.add_trace(go.Bar(
        x=df_kid_ingredients['Ingredient'],
        y=df_kid_ingredients['Daily Demand'],
        name='Daily Demand',
        marker_color='green',
        text=df_kid_ingredients['Daily Demand'],
        textposition='auto',
        textfont=dict(size=14)
    ))

    # Add bars for monthly demand
    fig.add_trace(go.Bar(
        x=df_kid_ingredients['Ingredient'],
        y=df_kid_ingredients['Monthly Demand'],
        name='Monthly Demand',
        marker_color='blue',  # Change color for distinction
        text=df_kid_ingredients['Monthly Demand'],
        textposition='auto',
        textfont=dict(size=14)
    ))

    # Update layout
    fig.update_layout(
        title='Daily and Monthly Demand of Kid Friendly Guacamole Ingredients',
        xaxis_title='Ingredients',
        yaxis_title='Demand',
        barmode='group',  # Group bars together
        template='plotly_white'  # Optional: change template for better visuals
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig)

# Demand for fiery guacamole ingredients
with col3:
    daily_demand_avocado_fiery = avocado_fiery * fiery_demand
    daily_demand_lime_fiery = lime_fiery * fiery_demand
    daily_demand_jalapeno_chili_fiery = jalapeno_chili_fiery * fiery_demand
    daily_demand_onion_fiery = onion_fiery * fiery_demand
    daily_demand_tobasco_fiery = tobasco_fiery * fiery_demand

    # Data
    monthly_demand_data = {
        'Ingredient': ['Avocado', 'Lime', 'Mayonnaise', 'Tomato', 'Garlic'],
        'Daily Demand': [
            daily_demand_avocado_fiery,
            daily_demand_lime_fiery,
            daily_demand_jalapeno_chili_fiery,
            daily_demand_onion_fiery,
            daily_demand_tobasco_fiery
        ]
    }

    # Create a DataFrame
    df_fiery_ingredients = pd.DataFrame(monthly_demand_data)

    # Calculate monthly demand (assuming 30 days)
    df_fiery_ingredients['Monthly Demand'] = df_fiery_ingredients['Daily Demand'] * 30

    # Create a bar plot using Plotly
    fig = go.Figure()

    # Add bars for daily demand
    fig.add_trace(go.Bar(
        x=df_fiery_ingredients['Ingredient'],
        y=df_fiery_ingredients['Daily Demand'],
        name='Daily Demand',
        marker_color='green',
        text=df_fiery_ingredients['Daily Demand'],
        textposition='auto',
        textfont=dict(size=14)
    ))

    # Add bars for monthly demand
    fig.add_trace(go.Bar(
        x=df_fiery_ingredients['Ingredient'],
        y=df_fiery_ingredients['Monthly Demand'],
        name='Monthly Demand',
        marker_color='blue',  # Change color for distinction
        text=df_fiery_ingredients['Monthly Demand'],
        textposition='auto',
        textfont=dict(size=14)
    ))

    # Update layout
    fig.update_layout(
        title='Daily and Monthly Demand of Fiery Guacamole Ingredients',
        xaxis_title='Ingredients',
        yaxis_title='Demand',
        barmode='group',  # Group bars together
        template='plotly_white'  # Optional: change template for better visuals
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig)

# Add a divider
st.divider()

# Ingredients costing
st.markdown("<h2 style='text-align: center;'>Ingredients Costing</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

# Supplier table
with col1:
    # Define the path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'supplier-ingredients.CSV')

    # Read the CSV file into a pandas DataFrame, specifying the delimiter
    df = pd.read_csv(csv_file_path, sep=';')

    # Convert 'Product-ID' column to string and remove any commas
    df['Product-ID'] = df['Product-ID'].astype(str).str.replace(',', '')

    # Convert 'Quantity' column to integer by removing commas first and then casting to int
    df['Quantity'] = df['Quantity'].astype(str).str.replace(',', '').astype(int)

    # Display the DataFrame without commas in 'Quantity' using `st.dataframe` and formatting options
    st.dataframe(df.style.format({"Quantity": "{:.0f}"}))

# Min price of ingredients wrt to latest date
with col2:
    # Adjust the column name as per your actual DataFrame structure
    ingredient_group = df.groupby('Product')

    # Create a DataFrame to store the minimum price for the most recent date
    min_price_recent_date = ingredient_group.apply(lambda x: x.loc[x['Date of Offer'].idxmax()]).reset_index(drop=True)

    # Find the minimum price from the selected rows for each ingredient
    result = min_price_recent_date.loc[min_price_recent_date.groupby('Product')['Price per Unit'].idxmin()]

    # Store the price in variables
    avocado_price = result.loc[result['Product'] == 'Avocado', 'Price per Unit'].values[0]
    coriander_price = result.loc[result['Product'] == 'Coriander', 'Price per Unit'].values[0]
    garlic_price = result.loc[result['Product'] == 'Garlic', 'Price per Unit'].values[0]
    jalapeno_chili_price = result.loc[result['Product'] == 'Jalapeno Chili', 'Price per Unit'].values[0]
    lime_price = result.loc[result['Product'] == 'Lime', 'Price per Unit'].values[0]
    mayonnaise_price = result.loc[result['Product'] == 'Mayonnaise', 'Price per Unit'].values[0]
    onion_price = result.loc[result['Product'] == 'Onion', 'Price per Unit'].values[0]
    red_chili_price = result.loc[result['Product'] == 'Red Chili', 'Price per Unit'].values[0]
    tabasco_price = result.loc[result['Product'] == 'Tabasco', 'Price per Unit'].values[0]
    red_chili_price = result.loc[result['Product'] == 'Red Chili', 'Price per Unit'].values[0]
    tomato_price = result.loc[result['Product'] == 'Tomato', 'Price per Unit'].values[0]

    # Display the message using st.markdown
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Avocado: <span style='color: green;'>{avocado_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Coriander: <span style='color: green;'>{coriander_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Garlic: <span style='color: green;'>{garlic_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Jalapeno Chili: <span style='color: green;'>{jalapeno_chili_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Lime: <span style='color: green;'>{lime_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Mayonnaise: <span style='color: green;'>{mayonnaise_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Onion: <span style='color: green;'>{onion_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Red Chili: <span style='color: green;'>{red_chili_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Tabasco: <span style='color: green;'>{tabasco_price}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: black;'>Price of Tomato: <span style='color: green;'>{tomato_price}</span></h5>", unsafe_allow_html=True)

# Cost of ingredients for producing Guacamole
col1, col2, col3 = st.columns(3)

# Cost of ingredients in Thai Guacamole
with col1:
    st.markdown("<h5 style='text-align: center;'>Cost of Ingredients for a Thai Guacamole</h5>", unsafe_allow_html=True)

    avocado_thai_cost = display_ingredient_cost(avocado_thai, avocado_price, 'Avocado', 'Pcs.')
    lime_thai_cost = display_ingredient_cost(lime_thai, lime_price, 'Lime', 'Pcs.')
    red_chili_thai_cost = display_ingredient_cost(red_chili_thai, red_chili_price, 'Red Chili', 'Grams')
    onion_thai_cost = display_ingredient_cost(onion_thai, onion_price, 'Onion', 'Grams')
    coriander_thai_cost = display_ingredient_cost(coriander_thai, coriander_price, 'Coriander', 'Grams')
    total_thai_guacamole_ingredient_cost = avocado_thai_cost + lime_thai_cost + red_chili_thai_cost + onion_thai_cost + coriander_thai_cost
    total_thai_guacamole_ingredient_cost_formatted = f"{total_thai_guacamole_ingredient_cost:.2f}".replace('.', ',')
    st.markdown(
        f"<h6 style='text-align: left; color: black;'>Total cost of ingredients in Thai Guacamole: <span style='color: green;'>{total_thai_guacamole_ingredient_cost_formatted}</span></h6>",
        unsafe_allow_html=True)

# Cost of ingredients in Kid Friendly Guacamole
with col2:
    st.markdown("<h5 style='text-align: center;'>Cost of Ingredients for a Kid Friendly Guacamole</h5>", unsafe_allow_html=True)

    avocado_kid_cost = display_ingredient_cost(avocado_kid, avocado_price, 'Avocado', 'Pcs.')
    lime_kid_cost = display_ingredient_cost(lime_kid, lime_price, 'Lime', 'Pcs.')
    mayonnaise_kid_cost = display_ingredient_cost(mayonnaise_kid, mayonnaise_price, 'Mayonnaise', 'ml')
    tomato_kid_cost = display_ingredient_cost(tomato_kid, tomato_price, 'Tomato', 'Grams')
    garlic_kid_cost = display_ingredient_cost(garlic_kid, garlic_price, 'Garlic', 'Grams')
    total_kid_guacamole_ingredient_cost = avocado_kid_cost + lime_kid_cost + mayonnaise_kid_cost + tomato_kid_cost + garlic_kid_cost
    total_kid_guacamole_ingredient_cost_formatted = f"{total_kid_guacamole_ingredient_cost:.2f}".replace('.', ',')
    st.markdown(
        f"<h6 style='text-align: left; color: black;'>Total cost of ingredients in Thai Guacamole: <span style='color: green;'>{total_kid_guacamole_ingredient_cost_formatted}</span></h6>",
        unsafe_allow_html=True)

# Cost of ingredients in Kid Friendly Guacamole
with col3:
    st.markdown("<h5 style='text-align: center;'>Cost of Ingredients for a Fiery Guacamole</h5>", unsafe_allow_html=True)

    avocado_fiery_cost = display_ingredient_cost(avocado_fiery, avocado_price, 'Avocado', 'Pcs.')
    lime_fiery_cost = display_ingredient_cost(lime_fiery, lime_price, 'Lime', 'Pcs.')
    jalapeno_fiery_cost = display_ingredient_cost(jalapeno_chili_fiery, jalapeno_chili_price, 'Jalapenos', 'Grams')
    onion_fiery_cost = display_ingredient_cost(onion_fiery, onion_price, 'Onion', 'Grams')
    tobasco_fiery_cost = display_ingredient_cost(tobasco_fiery, tabasco_price, 'Tobasco', 'ml')
    total_fiery_guacamole_ingredient_cost = avocado_fiery_cost + lime_fiery_cost + jalapeno_fiery_cost + onion_fiery_cost + tobasco_fiery_cost
    total_fiery_guacamole_ingredient_cost_formatted = f"{total_fiery_guacamole_ingredient_cost:.2f}".replace('.', ',')
    st.markdown(
        f"<h6 style='text-align: left; color: black;'>Total cost of ingredients in Thai Guacamole: <span style='color: green;'>{total_fiery_guacamole_ingredient_cost_formatted}</span></h6>",
        unsafe_allow_html=True)

# Cost for producing guacamole
thai_guacamole_monthly_ingredient_cost = round(total_thai_guacamole_ingredient_cost * thai_monthly_demand, 2)
kid_guacamole_monthly_ingredient_cost = round(total_kid_guacamole_ingredient_cost * kid_monthly_demand, 2)
fiery_guacamole_monthly_ingredient_cost = round(total_fiery_guacamole_ingredient_cost * fiery_monthly_demand, 2)
data = [
    {'Product': 'Thai Gucamole', 'Monthly Cost': thai_guacamole_monthly_ingredient_cost},
    {'Product': 'Kid Friendly Gucamole', 'Monthly Cost': kid_guacamole_monthly_ingredient_cost},
    {'Product': 'Fiery Gucamole', 'Monthly Cost': fiery_guacamole_monthly_ingredient_cost}
]
df_ingredient_cost = pd.DataFrame(data)

# Chart
total_monthly_ingredient_cost = df_ingredient_cost['Monthly Cost'].sum()
total_data = pd.DataFrame({
    'Product': ['Total Monthly Cost'],
    'Monthly Cost': [total_monthly_ingredient_cost]
})
df_total = pd.concat([df_ingredient_cost, total_data], ignore_index=True)
fig = px.bar(df_total, x='Product', y='Monthly Cost',
             title='Monthly Guacamole Ingredients Cost',
             labels={'Monthly Cost': 'Cost in EUR'},
             color='Product',
             text_auto='Monthly Cost')
fig.update_layout(yaxis_title='Monthly Cost',
                  xaxis_title='Products',
                  xaxis_tickangle=-45)
st.plotly_chart(fig)

# Add a divider
st.divider()

# Enter selling prices
st.sidebar.header("Guacamole Selling Prices")
with st.sidebar.expander("Enter Guacamole Selling Prices", expanded=False):
    selling_price_thai_guacamole = st.number_input('Thai Guacamole Selling Price:', min_value=0.0, max_value=100.0, value=11.0)
    selling_price_kid_guacamole = st.number_input('Kid Friendly Guacamole Selling Price:', min_value=0.0, max_value=100.0, value=12.5)
    selling_price_fiery_guacamole = st.number_input('Fiery Guacamole Selling Price:', min_value=0.0, max_value=100.0, value=12.0)

# Per month revenue
st.markdown("<h2 style='text-align: center;'>Guacamole Revenue</h2>", unsafe_allow_html=True)
monthly_revenue_thai_guacamole = round(selling_price_thai_guacamole * thai_monthly_demand, 2)
monthly_revenue_kid_guacamole = round(selling_price_kid_guacamole * kid_monthly_demand, 2)
monthly_revenue_fiery_guacamole = round(selling_price_fiery_guacamole * fiery_monthly_demand, 2)
data = [
    {'Product': 'Thai Gucamole', 'Monthly Revenue': monthly_revenue_thai_guacamole},
    {'Product': 'Kid Friendly Gucamole', 'Monthly Revenue': monthly_revenue_kid_guacamole},
    {'Product': 'Fiery Gucamole', 'Monthly Revenue': monthly_revenue_fiery_guacamole}
]
df = pd.DataFrame(data)

# Chart
total_monthly_revenue = df['Monthly Revenue'].sum()
total_data = pd.DataFrame({
    'Product': ['Total Monthly Revenue'],
    'Monthly Revenue': [total_monthly_revenue]
})
df_total = pd.concat([df, total_data], ignore_index=True)
fig = px.bar(df_total, x='Product', y='Monthly Revenue',
             title='Monthly Guacamole Revenue',
             labels={'Monthly Revenue'},
             color='Product',
             text_auto='Monthly Revenue')
fig.update_layout(yaxis_title='Monthly Revenue',
                  xaxis_title='Products',
                  xaxis_tickangle=-45)
st.plotly_chart(fig)

# Add a divider
st.divider()

# Enter fixed costs
st.sidebar.header("Fixed Costs")
with st.sidebar.expander("Enter Fixed Costs", expanded=False):
    rent = st.number_input('Rent:', min_value=0.0, max_value=20000.0, value=1500.0)
    salary = st.number_input('Salary:', min_value=0.0, max_value=20000.0, value=1250.0)

# Enter inputs for variable costs
st.sidebar.header("Variable Costs")
with st.sidebar.expander("Enter Variable Costs", expanded=False):

    # Direct variable costs
    variable_salary = st.number_input('Variable Food Salary:', min_value=0.0, max_value=100.0, value=11.0)
    variable_energy = st.number_input('Variable Food Energy Cost:', min_value=0.0, max_value=100.0, value=4.5)
    variable_other = st.number_input('Variable Food Other Costs:', min_value=0.00, max_value=100.00, value=2.75)

    # For thai guacamole recipe
    tg1 = st.number_input('TG1 mins.:', min_value=0, max_value=100, value=7,
                          help='TG: Thai Guacamole. Place avocados and lime or lemon juice in a medium bowl and roughly mash with a fork. Season to taste.')
    tg1s = st.number_input('TG1 sec.:', min_value=0, max_value=100, value=0,
                          help='TG: Thai Guacamole. Place avocados and lime or lemon juice in a medium bowl and roughly mash with a fork. Season to taste.')
    tg2 = st.number_input('TG2 mins.:', min_value=0, max_value=100, value=5,
                          help='TG: Thai Guacamole. Stir through remaining ingredients, reserving some chilli, coriander and red onion to garnish.')
    tg2s = st.number_input('TG2 sec.:', min_value=0, max_value=100, value=0,
                          help='TG: Thai Guacamole. Stir through remaining ingredients, reserving some chilli, coriander and red onion to garnish.')

    cooking_time_tg = tg1 + tg2 + (tg1s/60) + (tg2s/60)
    monthly_cooking_time_tg = (cooking_time_tg * thai_monthly_demand) / 60
    monthly_cooking_cost_tg = round(monthly_cooking_time_tg * (variable_salary + variable_energy + variable_other),2)

    # For kid friendly guacamole
    kfg1 = st.number_input('KFG1 mins.:', min_value=0, max_value=100, value=7,
                          help='KFG: Kid Friendly Guacamole. Place avocados and lime or lemon juice in a medium bowl and mash with a fork. Season to taste.')
    kfg1s = st.number_input('KFG1 sec.:', min_value=0, max_value=100, value=25,
                          help='KFG: Kid Friendly Guacamole. Place avocados and lime or lemon juice in a medium bowl and mash with a fork. Season to taste.')
    kfg2 = st.number_input('KFG2 mins.:', min_value=0, max_value=100, value=5,
                          help='KFG: Kid Friendly Guacamole. Add mayonnaise, garlic and 3/4 quarters of the tomato. Stir until combined.')
    kfg2s = st.number_input('KFG2 sec.:', min_value=0, max_value=100, value=0,
                          help='KFG: Kid Friendly Guacamole. Add mayonnaise, garlic and 3/4 quarters of the tomato. Stir until combined.')
    kfg3 = st.number_input('KFG3 mins.:', min_value=0, max_value=100, value=3,
                          help='KFG: Kid Friendly Guacamole. Garnish with reserved chopped tomato.')
    kfg3s = st.number_input('KFG3 sec.:', min_value=0, max_value=100, value=0,
                          help='KFG: Kid Friendly Guacamole. Garnish with reserved chopped tomato.')

    cooking_time_kfg = kfg1 + kfg2 + kfg3 + (kfg1s / 60) + (kfg2s / 60) + (kfg3s/60)
    monthly_cooking_time_kfg = (cooking_time_kfg * kid_monthly_demand) / 60
    monthly_cooking_cost_kfg = round(monthly_cooking_time_kfg * (variable_salary + variable_energy + variable_other),2)

    # For fiery guacamole
    fg1 = st.number_input('FG1 mins.:', min_value=0, max_value=100, value=7,
                          help='FG: Fiery Guacamole. Place avocados and lime or lemon juice in a medium bowl and mash with a fork. Season to taste.')
    fg1s = st.number_input('FG1 sec.:', min_value=0, max_value=100, value=0,
                          help='FG: Fiery Guacamole. Place avocados and lime or lemon juice in a medium bowl and mash with a fork. Season to taste.')
    fg2 = st.number_input('FG2 mins.:', min_value=0, max_value=100, value=3,
                          help='FG: Fiery Guacamole. Stir through remaining ingredients, reserving some red onion for garnish.')
    fg2s = st.number_input('FG2 sec.:', min_value=0, max_value=100, value=0,
                          help='FG: Fiery Guacamole. Stir through remaining ingredients, reserving some red onion for garnish.')
    fg3 = st.number_input('FG3 mins.:', min_value=0, max_value=100, value=5,
                          help='FG: Fiery Guacamole. Garnish with extra jalapeno slices, reserved red onion and micro-herbs if desired.')
    fg3s = st.number_input('FG3 sec.:', min_value=0, max_value=100, value=0,
                          help='FG: Fiery Guacamole. Garnish with extra jalapeno slices, reserved red onion and micro-herbs if desired.')

    cooking_time_fg = fg1 + fg2 + fg3 + (fg1s / 60) + (fg2s / 60) + (fg3s/60)
    monthly_cooking_time_fg = (cooking_time_fg * fiery_monthly_demand) / 60
    monthly_cooking_cost_fg = round(monthly_cooking_time_fg * (variable_salary + variable_energy + variable_other),2)

# Financial analysis
st.markdown("<h2 style='text-align: center;'>Financial Analysis</h2>", unsafe_allow_html=True)

# Calculations
data = [
    {'Category': 'Rent', 'Amount': rent},
    {'Category': 'Salary', 'Amount': salary}
]
df = pd.DataFrame(data)

total_fixed_cost = df['Amount'].sum()
total_variable_cost = monthly_cooking_cost_fg + monthly_cooking_cost_kfg + monthly_cooking_cost_tg
total_ingredients_cost = fiery_guacamole_monthly_ingredient_cost + kid_guacamole_monthly_ingredient_cost + thai_guacamole_monthly_ingredient_cost
total_cost = total_variable_cost + total_fixed_cost + total_ingredients_cost
profit = round(total_monthly_revenue - total_cost,2)

# Display cost revenue and profit
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"{total_monthly_revenue / 1000:.1f}k")
col2.metric("Total Cost", f"{total_cost / 1000:.1f}k")
col3.metric("Profit", f"{profit / 1000:.1f}k")

# Chart for total cost revenue and profit
data = [
    {'Category': 'Total Revenue', 'Amount': total_monthly_revenue},
    {'Category': 'Total Cost', 'Amount': total_cost},
    {'Category': 'Profit', 'Amount': profit}
]
df = pd.DataFrame(data)
# Create a single gauge chart with multiple labels and values
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=profit,
    title={'text': "Profit"},
    delta={'reference': total_cost, 'relative': False},
    gauge={
        'axis': {'range': [0, total_monthly_revenue]},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, total_cost], 'color': "red"},
            {'range': [total_cost, total_monthly_revenue], 'color': "yellow"}
        ],
        'threshold': {
            'line': {'color': "blue", 'width': 4},
            'thickness': 0.75,
            'value': profit
        }
    }
))

# Add additional annotations for Total Revenue and Total Cost
fig.add_trace(go.Indicator(
    mode="number",
    value=total_monthly_revenue,
    title={'text': "Total Revenue"},
    domain={'x': [0.1, 0.3], 'y': [0.1, 0.3]}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=total_cost,
    title={'text': "Total Cost"},
    domain={'x': [0.7, 0.9], 'y': [0.1, 0.3]}
))

# Update layout for better visibility
fig.update_layout(
    margin=dict(l=50, r=50, t=50, b=50)
)

# Display the chart in Streamlit
st.plotly_chart(fig)

# Add a divier
st.divider()

# BE analysis
st.markdown("<h2 style='text-align: center;'>Break Even Analysis</h2>", unsafe_allow_html=True)

# 3 cols for each product
col1, col2, col3 = st.columns(3)

# Calculate the variable cost per unit for tg
with col1:
    st.markdown("<h5 style='text-align: center;'>Thai Guacamole</h5>", unsafe_allow_html=True)
    unit_vc_tg = round((total_variable_cost / 3) / thai_monthly_demand, 2)
    st.metric(label='Avg. Unit Variable Cost', value=unit_vc_tg)
    st.metric(label='Price', value=selling_price_thai_guacamole)
    st.metric(label='Avg. Fixed Cost', value=round(total_fixed_cost/3,2))

    # Create df
    units = [0, 100, 200, 300, 400, 500, 600, 700, 800 ,900, 1000, 1100, 1200]
    df_thai_be = pd.DataFrame({
        'Units': units
    })
    df_thai_be['Price'] = selling_price_thai_guacamole
    df_thai_be['VC per Unit'] = unit_vc_tg
    df_thai_be['Total VC'] = df_thai_be['Units'] * df_thai_be['VC per Unit']
    df_thai_be['Fixed Cost'] = round(total_fixed_cost/3,2)
    df_thai_be['Total Cost'] = df_thai_be['Fixed Cost'] + df_thai_be['Total VC']
    df_thai_be['Total Revenue'] = df_thai_be['Units'] * df_thai_be['Price']
    df_thai_be['Profit/Loss'] = df_thai_be['Total Revenue'] - df_thai_be['Total Cost']
    df_thai_be['BE Units'] = round(df_thai_be['Fixed Cost']/(df_thai_be['Price']-df_thai_be['VC per Unit']),0)

    # Create chart
    # Create traces using DataFrame
    cost_trace = go.Scatter(
        x=df_thai_be['Units'],
        y=df_thai_be['Total Cost'],
        mode='lines',
        name='Total Cost',
        line=dict(color='red')
    )

    revenue_trace = go.Scatter(
        x=df_thai_be['Units'],
        y=df_thai_be['Total Revenue'],
        mode='lines',
        name='Total Revenue',
        line=dict(color='green')
    )

    # Break-even point
    break_even_x = df_thai_be['BE Units'].mean()
    break_even_y = df_thai_be['Total Cost'][df_thai_be['Units'].idxmax()]

    # Create a layout
    layout = go.Layout(
        title='Break-even Analysis',
        xaxis=dict(title='Units Sold'),
        yaxis=dict(title='EUR'),
        showlegend=True
    )

    # Create a figure
    fig = go.Figure(data=[cost_trace, revenue_trace], layout=layout)

    # Add break-even line
    fig.add_trace(go.Scatter(
        x=[break_even_x, break_even_x],
        y=[0, break_even_y],
        mode='lines',
        name='Break-even line',
        line=dict(color='blue', dash='dash')
    ))

    # Add break-even value annotation
    fig.add_annotation(
        x=break_even_x,
        y=break_even_y,
        text=f'{int(break_even_x)}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,  # Adjust vertical position
        font=dict(color='blue')
    )

    # Show plot in Streamlit app
    st.plotly_chart(fig)

# Calculate the variable cost per unit for kfg
with col2:
    st.markdown("<h5 style='text-align: center;'>Kid Friendly Guacamole</h5>", unsafe_allow_html=True)
    unit_vc_kfg = round((total_variable_cost / 3) / kid_monthly_demand, 2)
    st.metric(label='Avg. Unit Variable Cost', value=unit_vc_kfg)
    st.metric(label='Price', value=selling_price_kid_guacamole)
    st.metric(label='Avg. Fixed Cost', value=round(total_fixed_cost/3,2))

    # Create df
    units = [0, 100, 200, 300, 400, 500, 600, 700, 800 ,900, 1000, 1100, 1200]
    df_thai_kfg = pd.DataFrame({
        'Units': units
    })
    df_thai_kfg['Price'] = selling_price_kid_guacamole
    df_thai_kfg['VC per Unit'] = unit_vc_kfg
    df_thai_kfg['Total VC'] = df_thai_kfg['Units'] * df_thai_kfg['VC per Unit']
    df_thai_kfg['Fixed Cost'] = round(total_fixed_cost/3,2)
    df_thai_kfg['Total Cost'] = df_thai_kfg['Fixed Cost'] + df_thai_kfg['Total VC']
    df_thai_kfg['Total Revenue'] = df_thai_kfg['Units'] * df_thai_kfg['Price']
    df_thai_kfg['Profit/Loss'] = df_thai_kfg['Total Revenue'] - df_thai_kfg['Total Cost']
    df_thai_kfg['BE Units'] = round(df_thai_kfg['Fixed Cost']/(df_thai_kfg['Price']-df_thai_kfg['VC per Unit']),0)

    # Create chart
    # Create traces using DataFrame
    cost_trace = go.Scatter(
        x=df_thai_kfg['Units'],
        y=df_thai_kfg['Total Cost'],
        mode='lines',
        name='Total Cost',
        line=dict(color='red')
    )

    revenue_trace = go.Scatter(
        x=df_thai_kfg['Units'],
        y=df_thai_kfg['Total Revenue'],
        mode='lines',
        name='Total Revenue',
        line=dict(color='green')
    )

    # Break-even point
    break_even_x = df_thai_kfg['BE Units'].mean()
    break_even_y = df_thai_kfg['Total Cost'][df_thai_kfg['Units'].idxmax()]

    # Create a layout
    layout = go.Layout(
        title='Break-even Analysis',
        xaxis=dict(title='Units Sold'),
        yaxis=dict(title='EUR'),
        showlegend=True
    )

    # Create a figure
    fig = go.Figure(data=[cost_trace, revenue_trace], layout=layout)

    # Add break-even line
    fig.add_trace(go.Scatter(
        x=[break_even_x, break_even_x],
        y=[0, break_even_y],
        mode='lines',
        name='Break-even line',
        line=dict(color='blue', dash='dash')
    ))

    # Add break-even value annotation
    fig.add_annotation(
        x=break_even_x,
        y=break_even_y,
        text=f'{int(break_even_x)}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,  # Adjust vertical position
        font=dict(color='blue')
    )

    # Show plot in Streamlit app
    st.plotly_chart(fig)

# Calculate the variable cost per unit for fg
with col3:
    st.markdown("<h5 style='text-align: center;'>Fiery Guacamole</h5>", unsafe_allow_html=True)
    unit_vc_fg = round((total_variable_cost / 3) / fiery_monthly_demand, 2)
    st.metric(label='Avg. Unit Variable Cost', value=unit_vc_fg)
    st.metric(label='Price', value=selling_price_fiery_guacamole)
    st.metric(label='Avg. Fixed Cost', value=round(total_fixed_cost/3,2))

    # Create df
    units = [0, 100, 200, 300, 400, 500, 600, 700, 800 ,900, 1000, 1100, 1200]
    df_thai_fg = pd.DataFrame({
        'Units': units
    })
    df_thai_fg['Price'] = selling_price_fiery_guacamole
    df_thai_fg['VC per Unit'] = unit_vc_fg
    df_thai_fg['Total VC'] = df_thai_fg['Units'] * df_thai_fg['VC per Unit']
    df_thai_fg['Fixed Cost'] = round(total_fixed_cost/3,2)
    df_thai_fg['Total Cost'] = df_thai_fg['Fixed Cost'] + df_thai_fg['Total VC']
    df_thai_fg['Total Revenue'] = df_thai_fg['Units'] * df_thai_fg['Price']
    df_thai_fg['Profit/Loss'] = df_thai_fg['Total Revenue'] - df_thai_fg['Total Cost']
    df_thai_fg['BE Units'] = round(df_thai_fg['Fixed Cost']/(df_thai_fg['Price']-df_thai_fg['VC per Unit']),0)

    # Create chart
    # Create traces using DataFrame
    cost_trace = go.Scatter(
        x=df_thai_fg['Units'],
        y=df_thai_fg['Total Cost'],
        mode='lines',
        name='Total Cost',
        line=dict(color='red')
    )

    revenue_trace = go.Scatter(
        x=df_thai_fg['Units'],
        y=df_thai_fg['Total Revenue'],
        mode='lines',
        name='Total Revenue',
        line=dict(color='green')
    )

    # Break-even point
    break_even_x = df_thai_fg['BE Units'].mean()
    break_even_y = df_thai_fg['Total Cost'][df_thai_fg['Units'].idxmax()]

    # Create a layout
    layout = go.Layout(
        title='Break-even Analysis',
        xaxis=dict(title='Units Sold'),
        yaxis=dict(title='EUR'),
        showlegend=True
    )

    # Create a figure
    fig = go.Figure(data=[cost_trace, revenue_trace], layout=layout)

    # Add break-even line
    fig.add_trace(go.Scatter(
        x=[break_even_x, break_even_x],
        y=[0, break_even_y],
        mode='lines',
        name='Break-even line',
        line=dict(color='blue', dash='dash')
    ))

    # Add break-even value annotation
    fig.add_annotation(
        x=break_even_x,
        y=break_even_y,
        text=f'{int(break_even_x)}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,  # Adjust vertical position
        font=dict(color='blue')
    )

    # Show plot in Streamlit app
    st.plotly_chart(fig)