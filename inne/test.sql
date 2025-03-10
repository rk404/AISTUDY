-- Utwórz indeksy na często używanych kolumnach w klauzulach WHERE i JOIN
CREATE INDEX idx_rk_pozycje_dozr_id ON rk_pozycje (DOZR_ID);
CREATE INDEX idx_rk_dokumenty_id ON rk_dokumenty (id);
CREATE INDEX idx_rk_dokumenty_guid_dok_nadrz ON rk_dokumenty (GUID_DOK_NADRZ);
CREATE INDEX idx_pa_wrd_dokumenty_guid ON pa_wrd_dokumenty (GUID);
CREATE INDEX idx_ap_dokumenty_obrot_guid ON AP_DOKUMENTY_OBROT (GUID);
CREATE INDEX idx_cr_opportunities_oppo_number ON cr_opportunities (OPPO_NUMBER);

-- Użyj WITH clause, aby uniknąć powtarzania podzapytań
WITH NT_PA_DK_POZYCJE_GRUPY_271 AS (
    SELECT KOLUMNA1, KOLUMNA2
    FROM NT_PA_DK_POZYCJE_GRUPY
    WHERE GROB_ID = 271
),
NT_PA_DK_POZYCJE_GRUPY_207 AS (
    SELECT KOLUMNA1, KOLUMNA2
    FROM NT_PA_DK_POZYCJE_GRUPY
    WHERE GROB_ID = 207
)
SELECT dpoz.id, rd.KOD_SYSTEMU, substr(dpoz.KONT_SYMBOL,5,2) rodz_koszt,
       (SELECT KOLUMNA2 FROM NT_PA_DK_POZYCJE_GRUPY_271 WHERE KOLUMNA1 = substr(dpoz.KONT_SYMBOL,5,2)) NAZW_KOSZT,
       substr(dpoz.KONT_SYMBOL,8,9) zlec, wrd.SYMBOL symbol_dost, wrd.SYMBOL_KOLEJNY symbol, wrd.KONR_NAZWA,  wrd.guid dok_guid, 
       rd.IDENTYFIKATOR_KG, wrd.id dok_id, (dpoz.WN-dpoz.MA) Wartosc, substr(dpoz.KONT_SYMBOL,1,3) syntetyka  
FROM rk_pozycje dpoz
JOIN rk_dokumenty rd ON dpoz.DOZR_ID = rd.id
JOIN pa_wrd_dokumenty wrd ON rd.GUID_DOK_NADRZ = wrd.GUID 
where substr(dpoz.KONT_SYMBOL,1,3) = '081' and (dpoz.TYPD_PARAMETR='ZWY') AND rd.KOD_SYSTEMU = 'WRD'
UNION ALL
SELECT dpoz.id,rd.KOD_SYSTEMU, substr(dpoz.KONT_SYMBOL,5,2) rodz_koszt,
       (SELECT KOLUMNA2 FROM NT_PA_DK_POZYCJE_GRUPY_271 WHERE KOLUMNA1 = substr(dpoz.KONT_SYMBOL,5,2)) NAZW_KOSZT,
       substr(dpoz.KONT_SYMBOL,8,9) zlec, NULL AS symbol_dost, ado.SYMBOL, ado.KONR_NAZWA_SKR ,  ado.GUID dok_guid, rd.IDENTYFIKATOR_KG,
       ado.id dok_id, (dpoz.WN-dpoz.MA) Wartosc, substr(dpoz.KONT_SYMBOL,1,3) syntetyka   
FROM rk_pozycje dpoz
JOIN rk_dokumenty rd ON dpoz.DOZR_ID = rd.id
JOIN AP_DOKUMENTY_OBROT ado ON rd.GUID_DOK_NADRZ = ado.GUID 
where substr(dpoz.KONT_SYMBOL,1,3) = '081' and (dpoz.TYPD_PARAMETR='ZWY') AND rd.KOD_SYSTEMU = 'DOOB'
UNION ALL
SELECT dpoz.id,rd.KOD_SYSTEMU,  substr(dpoz.KONT_SYMBOL,5,2) rodz_koszt,
       (SELECT KOLUMNA2 FROM NT_PA_DK_POZYCJE_GRUPY_271 WHERE KOLUMNA1 = substr(dpoz.KONT_SYMBOL,5,2)) NAZW_KOSZT,
       substr(dpoz.KONT_SYMBOL,8,9) zlec, NULL AS symbol_dost, rd.SYMBOL_DOKUMENTU , rd.U_CRE,  rd.GUID dok_guid, rd.IDENTYFIKATOR_KG,
       rd.id dok_id, (dpoz.WN-dpoz.MA) Wartosc, substr(dpoz.KONT_SYMBOL,1,3) syntetyka  
FROM rk_pozycje dpoz
JOIN rk_dokumenty rd ON dpoz.DOZR_ID = rd.id
where substr(dpoz.KONT_SYMBOL,1,3) = '081' and (dpoz.TYPD_PARAMETR='ZWY') AND rd.KOD_SYSTEMU IN  ('FK','BANK','OS')
UNION ALL
SELECT dpoz.id,rd.KOD_SYSTEMU, 
       substr(dpoz.KONT_SYMBOL,17,3) rodz_koszt,
       (SELECT KOLUMNA2 FROM NT_PA_DK_POZYCJE_GRUPY_207 WHERE KOLUMNA1 = substr(dpoz.KONT_SYMBOL,17,3)) NAZW_KOSZT,
       substr(dpoz.KONT_SYMBOL,5,9) zlec, NULL AS symbol_dost, rd.SYMBOL_DOKUMENTU , rd.U_CRE,  rd.GUID dok_guid, rd.IDENTYFIKATOR_KG,
       rd.id dok_id, (dpoz.WN-dpoz.MA) Wartosc, substr(dpoz.KONT_SYMBOL,1,3) syntetyka 
FROM rk_pozycje dpoz
JOIN rk_dokumenty rd ON dpoz.DOZR_ID = rd.id
JOIN cr_opportunities OPPO on OPPO.OPPO_NUMBER = substr(dpoz.KONT_SYMBOL,5,9) and oppo.opty_id = 1
where 1=1
--AND rd.KOD_SYSTEMU IN  ('FK','BANK','OS')  
AND (dpoz.TYPD_PARAMETR='ZWY') 
AND substr(dpoz.KONT_SYMBOL,1,3) = '501';