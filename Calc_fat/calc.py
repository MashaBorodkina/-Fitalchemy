import streamlit as st

def calculate_body_fat(weight, height, gender, age):
    # Ваш алгоритм расчета уровня жира в теле
    if gender == 'Male':
        return 1.20 * weight/(height/100)**2 + 0.23 * age - 10.8-5.4
    elif gender == 'Female':
        return 1.20 * weight/(height/100)**2 + 0.23 * age - 5.4
    else:
        return None
    
def categorize_body_fat(age, body_fat, gender):
    if gender == 'Male':
        if age < 40:
            if body_fat < 14:
                return "Athletic Level", "green"
            elif body_fat < 18:
                return "Fitness Level", "lightgreen"
            elif body_fat < 25:
                return "Average Level", "orange"
            else:
                return "Overweight", "red"
        elif age < 60:
            if body_fat < 16:
                return "Athletic Level", "green"
            elif body_fat < 21:
                return "Fitness Level", "lightgreen"
            elif body_fat < 27:
                return "Average Level", "orange"
            else:
                return "Overweight", "red"
        else:
            if body_fat < 19:
                return "Athletic Level", "green"
            elif body_fat < 24:
                return "Fitness Level", "lightgreen"
            elif body_fat < 30:
                return "Average Level", "orange"
            else:
                return "Overweight", "red"
    
    elif gender == 'Female':
        if age < 40:
            if body_fat < 21:
                return "Athletic Level", "green"
            elif body_fat < 25:
                return "Fitness Level", "lightgreen"
            elif body_fat < 32:
                return "Average Level", "orange"
            else:
                return "Overweight", "red"
        elif age < 60:
            if body_fat < 23:
                return "Athletic Level", "green"
            elif body_fat < 28:
                return "Fitness Level", "lightgreen"
            elif body_fat < 35:
                return "Average Level", "orange"
            else:
                return "Overweight", "red"
        else:
            if body_fat < 24:
                return "Athletic Level", "green"
            elif body_fat < 30:
                return "Fitness Level", "lightgreen"
            elif body_fat < 36:
                return "Average Level", "orange"
            else:
                return "Overweight", "red"
# Описание для каждой категории
descriptions = {
    "Athletic Level": (
        "This level is typically associated with individuals engaged in high-level sports, either professionally or as a serious hobby. "
        "They have a high level of muscle mass and a low body fat percentage. This percentage of body fat ensures optimal physical fitness "
        "for maximum athletic performance. However, maintaining such a low level of fat requires regular training and a strict diet.\n\n"
        "Advantages: High performance, improved overall physical condition, lower risk of chronic diseases.\n\n"
        "Disadvantages: Can be difficult to maintain long-term without strict control over diet and training.\n\n"
        "<div style='color:blue;'> It is important to remember that this is only an approximate estimate. For more accurate measurements and health assessments,"
        "it is recommended to use additional methods, such as bioimpedance analysis or DEXA scanning,"
        "and to consider individual physiological characteristics.</div>"
    ),
    "Fitness Level": (
        "This level is characteristic of people who regularly engage in sports or fitness activities but are not at a professional level. "
        "They also have a low body fat percentage, but slightly higher than athletes. This is a healthy range that indicates good physical "
        "fitness and absence of excess weight.\n\n"
        "Advantages: Maintaining good physical fitness, reducing the risk of chronic diseases, accessible to a wider range of people.\n\n"
        "Disadvantages: May require regular physical activity and healthy eating to maintain.\n\n"
        "<div style='color:blue;'> It is important to remember that this is only an approximate estimate. For more accurate measurements and health assessments,"
        "it is recommended to use additional methods, such as bioimpedance analysis or DEXA scanning,"
        "and to consider individual physiological characteristics.</div>"
    ),
    "Average Level": (
        "This range characterizes the average physical condition, where a moderate amount of fat is present. This is the most common range among "
        "people leading a relatively active lifestyle but not engaged in intensive training. Fat levels in this range are considered normal for health.\n\n"
        "Advantages: Moderate risk of chronic diseases, a typical level for many people.\n\n"
        "Disadvantages: May indicate a need to increase physical activity to improve health and fitness.\n\n"
        "<span style='color:blue;'> It is important to remember that this is only an approximate estimate. For more accurate measurements and health assessments,"
        "it is recommended to use additional methods, such as bioimpedance analysis or DEXA scanning,"
        "and to consider individual physiological characteristics.</span>"
    ),
    "Overweight": (
        "A body fat percentage in this range indicates the presence of excess weight, which may lead to an increased risk of various diseases, such as "
        "cardiovascular diseases, type 2 diabetes, and other chronic conditions. People with this level of body fat are recommended to consult a specialist "
        "to adjust their lifestyle and diet.\n\n"
        "Advantages: No obvious benefits, but it is a signal that action is needed to improve health.\n\n"
        "Disadvantages: Increased risk of cardiovascular diseases, diabetes, hypertension, and other obesity-related conditions.\n\n"
        "<div style='color:blue;'> It is important to remember that this is only an approximate estimate. For more accurate measurements and health assessments,"
        "it is recommended to use additional methods, such as bioimpedance analysis or DEXA scanning,"
        "and to consider individual physiological characteristics.</div>"
    ),
}
    

st.title("Body Fat Calculator")
st.markdown("This calculator helps you determine your body fat percentage based on your weight, height, age, and gender. "
            "The body fat percentage norms provided below are based on widely accepted recommendations and studies, " 
            "which are comparable to estimates calculated using the Deurenberg & Womersley equation.")

weight = st.number_input("Weight (kg): Enter an integer", step=1)
height = st.number_input("Height (cm)", step=1)
gender = st.selectbox('Gender', options = ['Select an option','Male', 'Female'])
age = st.number_input('Age', min_value=0)

if st.button("Calculate"):
    if weight > 0 and height > 0 and age > 0:
        result = calculate_body_fat(weight, height, gender, age)
        
        if result is not None:
            st.write(f"Your body fat percentage is: {result:.2f}%")

            category, color = categorize_body_fat(age, result, gender)
            
            # Подсвечивание категории и вывод описания
            st.markdown(f"<h3 style='color:{color};'>{category}</h3>", unsafe_allow_html=True)
            st.markdown(descriptions[category], unsafe_allow_html=True)
        else:
            st.write("Error: To calculate the result, it's necessary to select a gender,"
                     "as the formula takes this parameter into account. If you do not identify "
                     "with a specific gender, you can choose the one that most closely aligns with "
                     "your physiological characteristics to achieve the most accurate result. "
                     "Thank you for your understanding!")
    else:
        st.write("Please enter all required values: weight, height, gender and age.")