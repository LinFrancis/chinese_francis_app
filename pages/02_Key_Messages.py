
import streamlit as st
from collections import defaultdict

st.set_page_config(page_title="林高天 Journey", layout="wide")
from sidebar_header import render_sidebar_header
render_sidebar_header()


st.title("Key messages in Chinese and English")
# Display settings


show_en = st.sidebar.checkbox("Mostrar Inglés (EN)", value=True)
show_zh = st.sidebar.checkbox("Mostrar Chino (中)", value=True)
show_py = st.sidebar.checkbox("Mostrar Pinyin (PY)", value=True)
expand_all = st.sidebar.checkbox("🔓 Expandir todos los bloques", value=False)

bloques = [
    ("🌍 Why regeneration?",
     "Around the world, nature is being destroyed.",
     "在世界各地，大自然正在被破坏。",
     "Zài shìjiè gèdì, dàzìrán zhèngzài bèi pòhuài."),

    ("", 
     "Biodiversity is disappearing. Healthy soil is being lost. We need organic agriculture, good composting, and food growing in the cities to protect nature and life.",
     "生物多样性正在消失，健康的土壤正在流失。我们需要有机农业、良好的堆肥和城市里的种植食物，来保护大自然和生命。",
     "Shēngwù duōyàngxìng zhèngzài xiāoshī, jiànkāng de tǔrǎng zhèngzài liúshī. Wǒmen xūyào yǒujī nóngyè, liánghǎo de duīfèi hé chéngshì lǐ de zhòngzhí shíwù, lái bǎohù dàzìrán hé shēngmìng."),

    ("", "Without nature, there is no future for people or for life.",
     "没有大自然，人类和生命就没有未来。",
     "Méiyǒu dàzìrán, rénlèi hé shēngmìng jiù méiyǒu wèilái."),

    ("", "I learned that nature can restore itself.",
     "我明白了大自然可以自己恢复。",
     "Wǒ míngbáile dàzìrán kěyǐ zìjǐ huīfù."),

    ("", "Nature can grow again, and life can continue.",
     "大自然可以重新成长，生命可以继续。",
     "Dàzìrán kěyǐ chóngxīn chéngzhǎng, shēngmìng kěyǐ jìxù."),

    ("", "This is what I call regeneration.",
     "这就是我说的“再生”。",
     "Zhè jiù shì wǒ shuō de “zàishēng”."),

    ("", "Regeneration is the hope and the action to bring life back.",
     "再生是希望，也是让生命回来的一种行动。",
     "Zàishēng shì xīwàng, yě shì ràng shēngmìng huílái de yī zhǒng xíngdòng."),

    ("", "That is the path I want to follow.",
     "这是我想走的路。",
     "Zhè shì wǒ xiǎng zǒu de lù."),

    ("👤 Who am I?",
     "Hello, my name is Francis.",
     "你好，我叫Francis。",
     "Nǐ hǎo, wǒ jiào Francis."),

    ("", "I live in Chile and I am a social sciences professional.",
     "我住在智利，是一名社会科学工作者。",
     "Wǒ zhù zài Zhìlì, shì yì míng shèhuì kēxué gōngzuò zhě."),

    ("", "I have been studying Mandarin Chinese for several years.",
     "我学习汉语很多年了。",
     "Wǒ xuéxí Hànyǔ hěn duō nián le."),

    ("", "I studied at the Confucius Institute and have visited China five times for short periods.",
     "我在孔子学院学习过，也去过中国五次，时间虽然不长，但每次都很特别。",
     "Wǒ zài Kǒngzǐ Xuéyuàn xuéxí guò, yě qù guò Zhōngguó wǔ cì, shíjiān suīrán bù cháng, dàn měi cì dōu hěn tèbié."),

    ("🎶 My love for Chinese culture and music",
     "I am deeply interested in China and its culture.",
     "我很喜欢中国和中国文化。",
     "Wǒ hěn xǐhuān Zhōngguó hé Zhōngguó wénhuà."),

    ("", "I greatly admire its history, philosophy, and its future vision as an eco-civilization.",
     "我对中国的历史、思想和“生态文明”的未来很有兴趣。",
     "Wǒ duì Zhōngguó de lìshǐ, sīxiǎng hé “shēngtài wénmíng” de wèilái hěn yǒu xìngqù."),

    ("", "I also love traditional Chinese music.",
     "我也很喜欢中国传统音乐。",
     "Wǒ yě hěn xǐhuān Zhōngguó chuántǒng yīnyuè."),

    ("", "I study the dizi and dongxiao flutes.",
     "我学习笛子和洞箫。",
     "Wǒ xuéxí dízi hé dòngxiāo."),

    ("", "Through music, I connect deeply with Chinese culture and also with myself.",
     "我觉得音乐可以让我和中国文化有很深的联系，也让我认识自己。",
     "Wǒ juéde yīnyuè kěyǐ ràng wǒ hé Zhōngguó wénhuà yǒu hěn shēn de liánxì, yě ràng wǒ rènshi zìjǐ."),

    ("🌱 What I do",
     "I participate in organizations like AUCCA and the Urban Agroecology Movement (MAU) in Chile.",
     "我在智利参加两个组织：AUCCA 和 城市农业运动（MAU）。",
     "Wǒ zài Zhìlì cānjiā liǎng gè zǔzhī: AUCCA hé chéngshì nóngyè yùndòng (MAU)."),

    ("", "We seek ways of life that respect nature, promote regeneration, and support collective well-being.",
     "我们想找到一种新的生活方法：和大自然一起生活，保护环境，让大家一起生活得更好。",
     "Wǒmen xiǎng zhǎodào yì zhǒng xīn de shēnghuó fāngfǎ: hé dàzìrán yīqǐ shēnghuó, bǎohù huánjìng, ràng dàjiā yīqǐ shēnghuó de gèng hǎo."),

    ("", "I also take part in Race to Resilience, a global campaign to strengthen resilience to climate change.",
     "我也参加了一个世界性的项目，叫 Race to Resilience，我们一起面对气候变化的问题。",
     "Wǒ yě cānjiā le yí gè shìjiè xìng de xiàngmù, jiào Race to Resilience, wǒmen yīqǐ miànduì qìhòu biànhuà de wèntí."),

    ("🔍 My learning goals in China",
     "I especially want to visit the Institute of Urban Agriculture in Chengdu, and also connect with other schools, organizations, and businesses working on regeneration in cities, so we can help and inspire each other.",
     "我特别想去成都的都市农业研究所，也想认识其他在城市里做再生工作的学校、机构和企业，我们可以互相帮助、互相启发。",
     "Wǒ tèbié xiǎng qù Chéngdū de dūshì nóngyè yánjiūsuǒ, yě xiǎng rènshi qítā zài chéngshì lǐ zuò zàishēng gōngzuò de xuéxiào, jīgòu hé qǐyè, wǒmen kěyǐ hùxiāng bāngzhù, hùxiāng qǐfā."),

    ("💫 Final thought",
     "I want to continue being a bridge between what’s happening in China and what we can build in Chile.",
     "我想做中国和智利之间的“桥”，一起建设更好的未来。",
     "Wǒ xiǎng zuò Zhōngguó hé Zhìlì zhī jiān de “qiáo”, yīqǐ jiànshè gèng hǎo de wèilái."),
]

# Group and display blocks
from collections import defaultdict
bloques_por_titulo = defaultdict(list)
current_title = "⮞ Other"

for titulo, en, zh, py in bloques:
    if titulo:
        current_title = titulo
    bloques_por_titulo[current_title].append((en, zh, py))

for titulo, items in bloques_por_titulo.items():
    with st.expander(titulo, expanded=expand_all):
        for en, zh, py in items:
            if show_en:
                st.markdown(f"**EN:** {en}")
            if show_zh:
                st.markdown(f"**中:** {zh}")
            if show_py:
                st.markdown(f"**PY:** *{py}*")
            st.markdown("---")


