void CImageProcessing2021108030Doc::OnHomogenOperatorThreshold()
{
	int i, j, n, m;
	double max, ** tempOutputImage;
	CHomogenOperatorThresholdDlg dlg;
	if (dlg.DoModal() == IDOK) {
		if (dlg.val1 > dlg.val2) {
			int temp = dlg.val1;
			dlg.val1 = dlg.val2;
			dlg.val2 = temp;
		}
		m_Re_width = m_width;
		m_Re_height = m_height;
		m_Re_size = m_Re_width * m_Re_height;
		m_OutputImage = new unsigned char[m_Re_size];

		m_tempImage = Image2DMem(m_height + 2, m_width + 2);
		tempOutputImage = Image2DMem(m_Re_height, m_Re_width);

		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				m_tempImage[i + 1][j + 1] = (double)m_InputImage[i * m_width + j];
			}
		}
		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				max = 0.0;
				for (n = 0; n < 3; n++) {
					for (m = 0; m < 3; m++) {
						if (DoubleABS(m_tempImage[i + 1][j + 1] - m_tempImage[i + n][j + m]) >= max)
							max = DoubleABS(m_tempImage[i + 1][j + 1] - m_tempImage[i + n][j + m]);
					}
				}
				if (dlg.val2 < max)
					max = 255.;
				else if (dlg.val1 <= max <= dlg.val2)
					max = dlg.val1;
				else if (dlg.val1 > max)
					max = 0.;
				tempOutputImage[i][j] = max;
			}
		}
		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				if (tempOutputImage[i][j] > 255.)
					tempOutputImage[i][j] = 255.;
				if (tempOutputImage[i][j] < 0.)
					tempOutputImage[i][j] = 0.;
			}
		}
		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				m_OutputImage[i * m_Re_width + j]
					= (unsigned char)tempOutputImage[i][j];
			}
		}
	}
}