describe('Flujo de Reserva TicketFast', () => {
  it('Debe crear una reserva VIP y verificar el total', () => {
    // 1. Navegar a la URL de la interfaz de reservas
    cy.visit('http://localhost:4200/reservas')

    // 2. Diligenciar el formulario
    cy.get('[data-testid="input-email-cliente"]').type('cliente-e2e@correo.com')
    cy.get('[data-testid="select-zona-evento"]').select('VIP')
    cy.get('[data-testid="input-cantidad-asientos"]').clear().type('1')

    // 3. Hacer clic en el botón de confirmación
    cy.get('[data-testid="btn-confirmar-reserva"]').click()

    // 4. Verificar utilizando mecanismos de aserción asincrónica (sin sleep)
    // Cypress automáticamente reintenta hasta que el elemento pase a contener el texto
    cy.get('[data-testid="seccion-resumen-total"]')
      .should('contain.text', '150.000')
  })
})
