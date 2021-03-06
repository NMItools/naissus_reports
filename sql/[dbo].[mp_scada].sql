USE [SANiN]
GO
/****** Object:  StoredProcedure [dbo].[mp_scada]    Script Date: 30-Oct-20 01:41:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[mp_scada] (
	@tabela as varchar(10)
	)
AS
-- =============================================
-- Author:		Nebojša Pešić
-- Create date: 2020-05-19
-- Description:	

-- EXECUTE [dbo].[mp_scada] 'SCADA_2020'

-- =============================================
BEGIN
	SET NOCOUNT ON;

DECLARE @cols as nvarchar(max)
DECLARE @query as nvarchar(max)

SET @cols = '[I-1-LJB],[I-BBV-2],[BBV_II-8],[I-2-DIV],[I-3-MOK],[I-4-KR1],[I-4-KR2],[I-V-6],[I-5-STU],[MRB],[III-8],[M-70-81-17],[I-7-M10],[I-7-M11],[I-7-M2],[I-6-MLJ],[M-20-992-13],[M-20-992-27],[M-170-992-34],[M-190-21-35],[M-100-120-9],[M-10-100-11],[M-10-20-1],[M-10-20-12],[M-10-40-3],[M-10-40-4],[M-10-50-5],[M-10-60-6],[M-10-80-7],[M-10-80-8],[M-10-90-10],[M-10-90-32],[M-120-150-28],[M-20-100-15],[M-20-30-14],[M-20-30-22],[M-20-40-18],[M-20-40-21],[M-20-50-23],[M-40-50-16],[M-50-60-19],[M-80-140-29],[M-90-91-20]'

SET @query = 'SELECT [vreme], ' + @cols + ' from (select [mm], [vreme], ISNULL([Q_poz],0) + ISNULL([Q_neg],0) as Q from [SANiN].[mz].[' + @tabela + ']) x
              PIVOT 
			  (
                sum([Q])
                for mm in (' + @cols + ')
              ) p'

EXECUTE(@query)

END
