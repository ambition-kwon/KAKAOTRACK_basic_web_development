void CImageProcessing2021108030Doc::OnBlurr()
{
	int i, j;
	double BlurrMask[5][5] = {{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.} };
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = OnMaskProcess(m_InputImage, BlurrMask);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_tempImage[i][j] += 128;
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)m_tempImage[i][j];
		}
	}
}