import streamlit as st

st.set_page_config(page_title="林高天 Journey", layout="wide")

from sidebar_header import render_sidebar_header
render_sidebar_header()

st.title("Personal learning companion")

# Sidebar language selection
lang_option = st.sidebar.radio("Select language display", (
    "Only EN",
    "EN + 中文",
    "EN + 中文 + Pinyin",
    "中文 + Pinyin only",
    "Only 中文"
))

# Text blocks (modular design)
content_blocks = [
    {
        "title": "Purpose",
        "en": "This is my personal Chinese learning space. The goal is to reach HSK 3 level by 2026 — through practice, reflection, and consistent vocabulary review.",
        "zh": "这是我个人学习中文的空间。我的目标是在2026年之前达到HSK三级水平 —— 通过练习、反思和持续的词汇复习来实现。",
        "py": "Zhè shì wǒ gèrén xuéxí Zhōngwén de kōngjiān. Wǒ de mùbiāo shì zài 2026 nián zhīqián dádào HSK sān jí shuǐpíng — tōngguò liànxí, fǎnsī hé chíxù de cíhuì fùxí lái shíxiàn."
    },
    {
        "title": "This app includes",
        "en": "- **Key Messages:** Meaningful sentences in English, Chinese, and Pinyin.\n- **Dictionary:** A word list up to HSK 3, searchable and organized.",
        "zh": "- **关键信息：** 英文、中文和拼音的有意义句子。\n- **词汇表：** HSK 3级及以下的单词列表，可搜索和分类。",
        "py": "- **Guānjiàn xìnxī:** Yīngwén, Zhōngwén hé pīnyīn de yǒu yìyì jùzi.\n- **Cíhuì biǎo:** HSK 3 jí jí yǐxià de dāncí lièbiǎo, kě sōusuǒ hé fēnlèi."
    },
    {
        "title": "Who am I?",
        "en": "My name is Francis Lin Gaotian. I am a sociologist, permaculture designer, and regenerative practitioner. I am the Data Officer for the Technical Secretariat of the global Race to Resilience campaign ([link](https://www.climatechampions.net/campaigns/race-to-resilience/)), hosted by the Centre for Climate and Resilience Research (CR2) in Chile ([link](https://www.cr2.cl/)).\n\nI hold a Master’s in Sociology and a Postgraduate Diploma in Chinese Studies. I also trained in permaculture design.\n\nI live in the city and I believe urban areas hold the key challenges and opportunities for transformation. I see myself as an expert urban regeneration agent, continually improving my relational skills to support necessary transitions.\n\nI am increasingly becoming a bridge between China’s ecological civilization project and the work I do in Chile and other global networks.",
        "zh": "我叫林高天，是一位社会学家、永续设计师和再生实践者。我是全球“复原力竞赛” ([链接](https://www.climatechampions.net/campaigns/race-to-resilience/)) 技术秘书处的数据官，该秘书处设在智利的气候与复原力研究中心（CR2） ([链接](https://www.cr2.cl/))。\n\n我拥有社会学硕士学位和中国研究的研究生文凭，也接受了永续设计方面的培训。\n\n我生活在城市里，相信城市是应对挑战与转型的关键。我是一位城市再生的专家，不断提升我的关系能力，以引导必要的变革。\n\n我越来越成为连接中国生态文明项目与我在智利和世界其他地方工作之间的桥梁。",
        "py": "Wǒ jiào Lín Gāotiān, shì yī wèi shèhuì xuéjiā, yǒngxù shèjì shī hé zàishēng shíjiàn zhě. Wǒ shì quánqiú 'Fùyuánlì jìngsài' ([liànjiē](https://www.climatechampions.net/campaigns/race-to-resilience/)) jìshù mìshū chù de shùjù guān, gāi mìshū chù shè zài Zhìlì de Qìhòu yǔ Fùyuánlì Yánjiū Zhōngxīn (CR2) ([liànjiē](https://www.cr2.cl/)).\n\nWǒ yǒngyǒu shèhuìxué shuòshì xuéwèi hé Zhōngguó yánjiū de yánjiūshēng wénpíng, yě jiēshòule yǒngxù shèjì fāngmiàn de péixùn.\n\nWǒ shēnghuó zài chéngshì lǐ, xiāngxìn chéngshì shì yìngduì tiǎozhàn yǔ zhuǎnxíng de guānjiàn. Wǒ shì yī wèi chéngshì zàishēng de zhuānjiā, bùduàn tíshēng wǒ de guānxì nénglì, yǐ yǐndǎo bìyào de biàngé.\n\nWǒ yuèláiyuè chéngwéi liánjiē Zhōngguó shēngtài wénmíng xiàngmù yǔ wǒ zài Zhìlì hé shìjiè qítā dìfāng gōngzuò zhī jiān de qiáoliáng."
    },
    {
        "title": "Notes for Myself",
        "en": "- All content is at or below HSK 3.\n- This app helps track progress.\n- I can also get support if needed.",
        "zh": "- 所有内容不超过HSK三级。\n- 此应用可帮助跟踪进度。\n- 在需要时可以获得支持。",
        "py": "- Suǒyǒu nèiróng bù chāoguò HSK sān jí.\n- Cǐ yìngyòng kě bāngzhù gēnzōng jìnbù.\n- Zài xūyào shí kěyǐ huòdé zhīchí."
    },
    {
        "title": "Contact Info",
        "en": "- WeChat: francismason\n- Email: francis.mason@gmail.com",
        "zh": "- 微信：francismason\n- 电子邮件：francis.mason@gmail.com",
        "py": "- Wēixìn: francismason\n- Diànzǐ yóujiàn: francis.mason@gmail.com"
    }
]

# Display based on selection
for block in content_blocks:
    with st.container():
        st.subheader(block["title"])

        if lang_option == "Only EN":
            st.markdown(f"{block['en']}")
        elif lang_option == "EN + 中文":
            st.markdown(f"{block['en']}")
            st.markdown(f"{block['zh']}")
        elif lang_option == "EN + 中文 + Pinyin":
            st.markdown(f"{block['en']}")
            st.markdown(f"{block['zh']}")
            st.markdown(f"*{block['py']}*")
        elif lang_option == "中文 + Pinyin only":
            st.markdown(f"{block['zh']}")
            st.markdown(f"*{block['py']}*")
        elif lang_option == "Only 中文":
            st.markdown(f"{block['zh']}")
