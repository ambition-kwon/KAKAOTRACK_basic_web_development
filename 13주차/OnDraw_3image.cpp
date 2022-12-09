void CImageProcessing2021108030View::OnDraw(CDC* pDC)
{
	CImageProcessing2021108030Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;
	
	int i, j;
	unsigned char R, G, B;

	
	for (i = 0; i < pDoc->m_height; i++) {
		for (j = 0; j < pDoc->m_width; j++) {
			R = G = B = pDoc->m_InputImage[i * pDoc->m_width + j];
			pDC->SetPixel(j + 5, i + 5, RGB(R, G, B));
		}
	}
	if (pDoc->m_MiddleImage == NULL) {
		for (i = 0; i < pDoc->m_Re_height; i++) {
			for (j = 0; j < pDoc->m_Re_width; j++) {
				R = pDoc->m_OutputImage[i * pDoc->m_Re_width + j];
				G = B = R;
				pDC->SetPixel(j + pDoc->m_width + 10, i + 5, RGB(R, G, B));
			}
		}
	}
	else {
		for (i = 0; i < pDoc->m_Re_height; i++) {
			for (j = 0; j < pDoc->m_Re_width; j++) {
				R = pDoc->m_MiddleImage[i * pDoc->m_Re_width + j];
				G = B = R;
				pDC->SetPixel(j + pDoc->m_width + 10, i + 5, RGB(R, G, B));
			}
		}
		for (i = 0; i < pDoc->m_Re_height; i++) {
			for (j = 0; j < pDoc->m_Re_width; j++) {
				R = pDoc->m_OutputImage[i * pDoc->m_Re_width + j];
				G = B = R;
				pDC->SetPixel(j + pDoc->m_width*2 + 20, i + 5, RGB(R, G, B));
			}
		}
	}
}