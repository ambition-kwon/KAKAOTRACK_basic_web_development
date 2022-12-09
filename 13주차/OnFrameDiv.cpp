void CImageProcessing2021108030Doc::OnFrameDiv()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	CImageFrameDlg dlg;
	int i;
	double alpha;
	if (dlg.DoModal() == IDOK) {
		alpha = dlg.m_Alpha;
		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		if (OpenDlg.DoModal() == IDOK) {
			File.Open(OpenDlg.GetFileName(), CFile::modeRead);
		}
		if (File.GetLength() == (unsigned)m_width * m_height) {
			m_MiddleImage = new unsigned char[m_size];
			File.Read(m_MiddleImage, m_size);
			File.Close();

			for (i = 0; i < m_size; i++) {
                //division exception처리를 위한 두개의 if문
				if (m_InputImage[i] == 0)
					m_OutputImage[i] = 0;
				else if (m_MiddleImage[i] == 0)
					m_OutputImage[i] = 255;
				else
					m_OutputImage[i] = (unsigned char)((alpha*m_InputImage[i]) / ((1-alpha)* m_MiddleImage[i]));
			}
		}
		else {
			AfxMessageBox("Image size not matched");
			return;
		}
	}
}