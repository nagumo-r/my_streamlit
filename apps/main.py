import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def app():
    st.title('Streamlit 入門')

    st.write("DataFrame")

    df  = pd.DataFrame({
        "1st row" : [i for i in range(4)],
        "2nd row" : [i*10 for i in range(4)]
    }
    )

    st.dataframe(df.style.highlight_max(axis = 0), 
                width = 600, height = 400
                )

    '''
    # 章
    ## 節
    ### 項

    ```python
    import streamlit as st
    import numpy as np
    import pandas as pd
    ```
    '''

    '''
    ### チャートの作成
    '''
    df2  = pd.DataFrame(
        np.random.rand(20,3),
        columns = ['A', 'B', 'C'],
    )
    st.line_chart(df2)
    st.area_chart(df2)
    st.bar_chart(df2)

    df3 = pd.DataFrame(
        np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
        columns = ['lat', 'lon']
    )

    st.map(df3)

    st.write('diplay image')

    img = Image.open(r".\apps\noel_clement.jpg")
    st.image(img, 
            caption = "noel clement skiing", 
            use_column_width = True
            )
