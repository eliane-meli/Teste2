function doGet() {
  try {
    // ID da sua planilha
    const SPREADSHEET_ID = '1iLftWtEUacg6iYCzZKhChR6b5nqrNQxTz6R3lulBCro';
    const SHEET_NAME = 'Expedido';
    
    // Conectar à planilha
    const spreadsheet = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = spreadsheet.getSheetByName(SHEET_NAME);
    
    // Obter dados
    const dataRange = sheet.getDataRange();
    const data = dataRange.getValues();
    
    // Processar dados (pular cabeçalho)
    const processedData = data.slice(1);
    
    // Retornar como JSON
    return ContentService
      .createTextOutput(JSON.stringify({
        success: true,
        data: processedData,
        lastUpdate: new Date().toISOString(),
        totalRecords: processedData.length
      }))
      .setMimeType(ContentService.MimeType.JSON)
      .setHeaders({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET'
      });
      
  } catch (error) {
    // Em caso de erro
    return ContentService
      .createTextOutput(JSON.stringify({
        success: false,
        error: error.toString(),
        lastUpdate: new Date().toISOString()
      }))
      .setMimeType(ContentService.MimeType.JSON)
      .setHeaders({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET'
      });
  }
}

function doPost(e) {
  return doGet(e);
}
