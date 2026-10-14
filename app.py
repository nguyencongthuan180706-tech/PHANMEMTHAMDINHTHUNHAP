import streamlit as st

# Tiêu đề ứng dụng
st.title("🏦 PHẦN MỀM THẨM ĐỊNH THU NHẬP KHÁCH HÀNG")
st.write("Nhập thông tin khách hàng để tính toán khả năng vay vốn.")

# Nhập thông tin khách hàng
STV = st.number_input(
    "Số tiền vay (VNĐ)",
    min_value=0,
    value=800_000_000,
    step=10_000_000
)

THV = st.number_input(
    "Thời hạn vay (năm)",
    min_value=1,
    value=5,
    step=1
)

LS = st.number_input(
    "Lãi suất vay (%/năm)",
    min_value=0.0,
    value=12.0,
    step=0.5
)

TN = st.number_input(
    "Thu nhập hàng tháng (VNĐ)",
    min_value=0,
    value=45_000_000,
    step=1_000_000
)

NC = st.number_input(
    "Khoản nợ cũ phải trả hàng tháng (VNĐ)",
    min_value=0,
    value=10_000_000,
    step=1_000_000
)

CPSH = st.number_input(
    "Chi phí sinh hoạt mỗi người/tháng (VNĐ)",
    min_value=0,
    value=4_000_000,
    step=500_000
)

SN = st.number_input(
    "Số người trong gia đình",
    min_value=1,
    value=3,
    step=1
)

# Nút tính toán
if st.button("TÍNH CHỈ SỐ DTI"):
    if TN <= CPSH * SN:
        st.error("Thu nhập không đủ chi trả chi phí sinh hoạt!")
    elif THV <= 0:
        st.error("Thời hạn vay phải lớn hơn 0!")
    else:
        # Tính số tiền gốc phải trả hàng tháng
        tien_goc_thang = STV / (THV * 12)

        # Tính tiền lãi phải trả hàng tháng
        tien_lai_thang = STV * (LS / 100 / 12)

        # Tổng tiền phải trả hàng tháng cho khoản vay mới
        tra_no_moi = tien_goc_thang + tien_lai_thang

        # Tổng nghĩa vụ trả nợ hàng tháng
        tong_no = tra_no_moi + NC

        # Thu nhập còn lại sau chi phí sinh hoạt
        thu_nhap_con_lai = TN - CPSH * SN

        # Tính chỉ số DTI
        DTI = tong_no / thu_nhap_con_lai

        # Hiển thị kết quả
        st.subheader("📊 KẾT QUẢ")

        st.metric(
            label="Chỉ số DTI",
            value=f"{DTI * 100:.2f}%"
        )

        st.write(f"**Tiền gốc trả hàng tháng:** {tien_goc_thang:,.0f} VNĐ")
        st.write(f"**Tiền lãi trả hàng tháng:** {tien_lai_thang:,.0f} VNĐ")
        st.write(f"**Tổng nợ phải trả hàng tháng:** {tong_no:,.0f} VNĐ")
        st.write(f"**Thu nhập còn lại sau sinh hoạt:** {thu_nhap_con_lai:,.0f} VNĐ")

        # Kết luận theo điều kiện đề bài
        if DTI < 0.7:
            st.error("✅ KẾT LUẬN: ĐƯỢC VAY")
        else:
            st.success("❌ KẾT LUẬN: KHÔNG ĐƯỢC VAY")
