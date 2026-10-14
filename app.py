# Kiểm tra dữ liệu
if TN <= 0:
    st.error("Thu nhập hàng tháng phải lớn hơn 0.")
else:
    # Tính tiền gốc phải trả hàng tháng
    tien_goc_thang = STV / (THV * 12)

    # Tính tiền lãi phải trả hàng tháng
    tien_lai_thang = STV * (LS / 100 / 12)

    # Tổng nghĩa vụ trả nợ hàng tháng
    tong_no_thang = tien_goc_thang + tien_lai_thang + NC

    # Chi phí sinh hoạt của gia đình
    tong_chi_phi_sinh_hoat = CPSH * SN

    # Thu nhập còn lại sau chi phí sinh hoạt
    thu_nhap_sau_sinh_hoat = TN - tong_chi_phi_sinh_hoat

    # Kiểm tra thu nhập sau sinh hoạt
    if thu_nhap_sau_sinh_hoat <= 0:
        st.error(
            "Thu nhập không đủ trang trải chi phí sinh hoạt. "
            "Không thể tính DTI theo công thức này."
        )
    else:
        # Tính chỉ số DTI
        DTI = tong_no_thang / thu_nhap_sau_sinh_hoat

        st.subheader("📊 KẾT QUẢ TÍNH TOÁN")

        col3, col4 = st.columns(2)

        with col3:
            st.metric(
                label="Chỉ số DTI",
                value=f"{DTI * 100:.2f}%"
            )

        with col4:
            st.metric(
                label="Ngưỡng DTI",
                value="70%"
            )

        # Hiển thị chi tiết
        with st.expander("Xem chi tiết cách tính"):
            st.write(
                f"**Tiền gốc phải trả/tháng:** "
                f"{tien_goc_thang:,.0f} VNĐ"
            )

            st.write(
                f"**Tiền lãi phải trả/tháng:** "
                f"{tien_lai_thang:,.0f} VNĐ"
            )

            st.write(
                f"**Tổng nghĩa vụ trả nợ/tháng:** "
                f"{tong_no_thang:,.0f} VNĐ"
            )

            st.write(
                f"**Tổng chi phí sinh hoạt/tháng:** "
                f"{tong_chi_phi_sinh_hoat:,.0f} VNĐ"
            )

            st.write(
                f"**Thu nhập sau sinh hoạt:** "
                f"{thu_nhap_sau_sinh_hoat:,.0f} VNĐ"
            )

            st.write(
                "**Công thức:** DTI = Tổng nghĩa vụ trả nợ "
                "/ Thu nhập sau sinh hoạt × 100%"
            )

            st.write(
                f"**Thay số:** DTI = "
                f"{tong_no_thang:,.0f} / "
                f"{thu_nhap_sau_sinh_hoat:,.0f} "
                f"× 100%"
            )

        # Kết luận theo yêu cầu
        if DTI < 0.70:
            st.error(
                "❌ KẾT LUẬN: KHÔNG ĐƯỢC VAY\n\n"
                "Chỉ số DTI nhỏ hơn 70%."
            )
        else:
            st.success(
                "✅ KẾT LUẬN: ĐƯỢC VAY\n\n"
                "Chỉ số DTI lớn hơn hoặc bằng 70%."
            )

        # Biểu đồ tiến độ DTI
        st.subheader("📈 Biểu đồ chỉ số DTI")

        st.progress(min(DTI, 1.0))

        st.write(f"DTI hiện tại: {DTI * 100:.2f}%")
        st.caption(
            "Lưu ý: Kết quả chỉ mang tính tham khảo theo quy tắc "
            "được thiết lập trong chương trình, không phải quyết "
            "định phê duyệt tín dụng thực tế của ngân hàng."
        )
